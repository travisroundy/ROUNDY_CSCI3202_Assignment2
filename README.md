# ROUNDY_CSCI3202_Assignment3

Usage: python Roundy_CSCI3202_Assignment3.py heuristic

-> heuristic is either a 1 or a 2.

------------------------------------------------------------------------

Heuristic 1 is the manhattan distance heuristic which takes straight
	line distances from the current node to the end.
	
Heuristic 2 is a diagonal distance from the current node to the goal.
	Similar to the heuristic, it tracks the distance from the current
	to the goal. However this allows for diagonals to be taken. The
	equation takes the Manhattan Distance multiplied the step distance
	and subtracts the same but allowing for diagonals.
		10*((endX-currX)+(endY-currY)) - (14 - 2*(10))*min((endX-currX),(endY-currY))
	The (14-2*(10)) is the distance saved from moving diagonally versus
	the 2 squares it takes to get the same distance with the manhattan.
	
	I believed this would be a sufficient heuristic because it is similar
	to the Manhattan Distance. Allowing for a more straight line distance
	to the goal node.
	
	When compared with the Manhattan Distance however, the total cost of
	the Diagonal Distance was about 300 larger (1690 vs. 1954). It did
	however count the same number of nodes when approaching the end node.
	
------------------------------------------------------------------------

I was not able to print out the correct path as I realized I was not
keeping track in another list. Due to that, I am also slightly off in 
my total cost calculations. The number of nodes evaluated however is
correct. I print out the closedNode list and acheive the total cost from
there which is incorrect but gives me close numbers.

By hand, I acheived a total value for Maze 1 of 1676, my program returns
1690.


