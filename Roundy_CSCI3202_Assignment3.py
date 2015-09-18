#Travis Roundy
#CSCI 3202 - Intro to AI
#Assignment 3

import sys
import math

class Node:
	def __init__(self):
		self.location = (0, 0)
		self.distanceToStart = (0) #g(n)
		self.heuristic = (0) #h(n)
		self.f = (0) #f(n) = g(n) + h(n)
		self.parent = (Node)
		self.value = None
		self.end = False
		self.reachable = None

class Astar:
	def __init__(self):
		self.openNodes = []
		self.closedNodes = set()
		self.maze = []
		self.endNode = (int, int)
		self.path = []
		
	def makeMaze(self, argv):
		for line in open(argv).readlines():
			self.maze.append(line.split())
		for i in range(0,8):
			for j in range(0,10):
				temp = self.maze[i][j]
				self.maze[i][j] = Node()
				self.maze[i][j].value = temp
				self.maze[i][j].location = (i,j)
				testvalue = self.maze[i][j].value
				#print("self.maze[i][j].value: %s" % testvalue)
				if (self.maze[i][j].value == '2'):
					self.maze[i][j].reachable = False
					#print("false areas: ",self.maze[i][j].location)
				elif (self.maze[i][j].value == '1'):
					#print("mountain")
					#self.maze[i][j].distanceToStart = self.maze[i][j].distanceToStart + 10
					self.maze[i][j].reachable = True
				else:
					self.maze[i][j].reachable = True

		#print(self.maze)
		
	def goUp(self,node):
		(x,y) = node.location
		newx = x - 1
		dist = node.distanceToStart + 10
		node.distanceToStart = dist		
		return newx
		
	def goDown(self,node):
		(x,y) = node.location
		newx = x + 1
		#dist = node.distanceToStart + 10
		#node.distanceToStart = dist
		return newx
		
	def goRight(self,node):
		(x,y) = node.location
		newy = y+1
		#dist = node.distanceToStart + 10
		#node.distanceToStart = dist
		return newy
	
	def goDiagUp(self,node):
		(x,y) = node.location
		newx = x - 1
		newy = y+1
		#dist = node.distanceToStart + 14
		#node.distanceToStart = dist
		return (newx,newy)
		
	def goDiagDown(self,node):
		(x,y) = node.location
		newx = x + 1
		newy = y + 1
		#dist = node.distanceToStart + 14
		#node.distanceToStart = dist
		return(newx,newy)
			
	
	def heuristic1(self, current):
		(cx,cy) = current.location
		(ex,ey) = self.endNode
		man_dist = (abs((ex - cx)) + abs((ey - cy))) * 10
		#print("Man_Dist = %s" % man_dist)
		return man_dist
		
	def heuristic2(self,current):
		(x,y) = current.location
		(ex,ey) = self.endNode
		dx = abs(ex - x)
		dy = abs(ey - y)
		return (10) * (dx+dy) - (14 - 2 * 10) * min(dx,dy)
		

	def AstarSearch(self,name, startx, starty, goalx, goaly, h):
		heuristic = int(h)
		self.makeMaze(name)
		self.maze[startx][starty].distanceToStart = 15000
		self.maze[startx][starty].parent = None
		self.maze[goalx][goaly].end = True
		self.endNode = self.maze[goalx][goaly].location
		self.openNodes.append(self.maze[startx][starty])
		#print("start: ",self.maze[startx][starty].location)
		counter = 0
		while (len(self.openNodes) != 0):
			#x = 0
			#y = 0
			z = 1500
			myNode = None
			testNode = None
			#print("1st myNode: ", myNode)
			for node in self.openNodes:
				#myNode 
				if node not in self.closedNodes:
					if node.f < z:
						testNode = node
					
			#print("myNode: ", myNode.f)
			currentNode = testNode
			#print("currentNode: ",currentNode.location)
			self.openNodes.remove(currentNode)
			self.closedNodes.add(currentNode)
			if (currentNode.end != True):
				count = 0
				(cx,cy) = currentNode.location
				while (count < 5):
					#print("count: %s" % count)
					if (count == 0):
						newx = self.goUp(currentNode)
						if ((newx <= 7) and (newx >= 0)):
							#print("0-nx ",newx)
							(cx,cy) = self.maze[newx][cy].location
							dist = self.maze[newx][cy].distanceToStart + 10
							self.maze[newx][cy].distanceToStart = dist
						else:
							count = count + 1

					elif (count == 1):
						newy = self.goRight(currentNode)
						if ((newy <= 9) and (newy >= 0)):
							#print("1-ny ",newy)
							(cx,cy) = self.maze[cx][newy].location
							dist = self.maze[cx][newy].distanceToStart + 10
							self.maze[cx][newy].distanceToStart = dist
						else:
							count = count + 1
							
					elif (count == 2):
						(newx,newy) = self.goDiagUp(currentNode)
						if ((newx <= 7) and (newy >= 0) and (newx >= 0) and (newy <= 9)):
							#print("2-nx,ny ",newx,newy)
							(cx,cy) = self.maze[newx][newy].location
							dist = self.maze[newx][newy].distanceToStart + 14
							self.maze[newx][newy].distanceToStart = dist
						else:
							count = count + 1					

					elif (count == 3):
						newx = self.goDown(currentNode)
						if ((newx <= 7) and (newx >= 0)):
							#print("3-nx ",newx)
							(cx,cy) = self.maze[newx][cy].location
							dist = self.maze[newx][cy].distanceToStart + 10
							self.maze[newx][cy].distanceToStart = dist
						else:
							count = count + 1
					elif (count == 4):
						(newx,newy) = self.goDiagDown(currentNode)
						if ((newx <= 7) and (newy >= 0) and (newx >= 0) and (newy <= 9)):
							#print("4-nx,ny ",newx,newy)
							(cx,cy) = self.maze[newx][newy].location
							dist = self.maze[newx][newy].distanceToStart + 14
							self.maze[newx][newy].distanceToStart = dist
						else:
							count = count + 1
					else:
						continue
					count = count + 1	
							
					#print("Checking Node: ", self.maze[cx][cy].location)
					if (self.maze[cx][cy].reachable != False) and (self.maze[cx][cy] != None):
						#self.maze[cx][cy].f = cx * 2
						man_dist = 0
						#print("heur: %s" % heuristic)
						if (heuristic == 1):
							man_dist = self.heuristic1(self.maze[cx][cy])
						elif (heuristic == 2):
							man_dist = self.heuristic2(self.maze[cx][cy])
						self.maze[cx][cy].heuristic = man_dist
						if (self.maze[cx][cy].value == '1'):
							#print("mountain")
							self.maze[cx][cy].distanceToStart = self.maze[cx][cy].distanceToStart + 14
						f = self.maze[cx][cy].distanceToStart + self.maze[cx][cy].heuristic
						#print("distance,heuristic: ",self.maze[cx][cy].distanceToStart, self.maze[cx][cy].heuristic)
						#print("Total Cost: ",f)
						
						if (self.maze[cx][cy] in self.openNodes):
							self.maze[cx][cy].parent = currentNode
							if (f < self.maze[cx][cy].f):
								self.maze[cx][cy].f = f
								
								
						else:
							#print("location in else: ",self.maze[cx][cy].location)
							self.maze[cx][cy].f = f
							self.maze[cx][cy].parent = currentNode
							self.openNodes.append(self.maze[cx][cy])
						
							
					else:
						
						continue
			else:					
				break
							
			#currentNode = None
			#counter = counter + 1
						

			#if counter == 2:
			#	break
			
		#print ("------------------------------------------------")
		
		totalcost = 0
		totalNodes = 0
		print("Path Taken: ")
		for node in self.closedNodes:
			if (node.parent != None):
				totalcost = totalcost + node.f
				totalNodes = totalNodes + 1
				myNode = node.parent
				print(myNode.location)
				#print(myNode.f)
				
			elif (node.parent == None):
				print(node.location)
				totalNodes = totalNodes + 1
				
		print("Total Cost: %s" % totalcost)
		print("Number of Nodes Evaluated: %s" % totalNodes)
		
		
if __name__ == "__main__":
	file_name = sys.argv[1]
	heuristic = sys.argv[2]
	h = Astar()
	h.AstarSearch(file_name, 7, 0, 0, 9, heuristic)
