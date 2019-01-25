import sys
import os
import heapq
from datetime import datetime
from random import shuffle
#try:
#    import Queue as Q  # ver. < 3.0
#except ImportError:
import queue as Q


class Puzzle:
    def __init__(self, arr):
        self.goal    = [1,2,3,8,0,4,7,6,5]
        self.state   = State(arr, None)
        self.initial = State(arr, None)
        self.isFinished = False
        self.arr = arr
# invoke solve method if need to use BFS
    def solve (self):
        print(str(datetime.now()))
        queue = Q.PriorityQueue() #[]
        successors = self.state.createSuccessors(queue, [])
        self.solveBFS(successors)
        print(str(datetime.now()))

    def solveBFS (self, queue):
        visited=[]
        i=0
        while not queue.empty():
            #state=heapq.heappop(queue)
            state=queue.get()
            if (state== self.goal):
                print("Victory!!")
                return  visited
            if not state in visited:
                visited.append(state)
                i+=1
                print(str(state)+" "+str(i))
                self.state.setArr(state)
                queue=self.state.createSuccessors(queue,visited)
        return  visited

    def solveDFS (self, visited, state):
        if self.isFinished==True:
            return
        if (state== self.goal):
                print("Victory!!")
                self.isFinished = True
                return  visited
        if not state in visited:
                visited.append(state)
                print(str(state))
                n=State(state, None)
                index_of_0 = self.arr.index(0)
                arr = n.moveUp(index_of_0)
                if (arr!=None):
                    self.solveDFS(visited, arr)
                arr1 = n.moveRight(index_of_0)
                if (arr1!=None):
                    self.solveDFS(visited, arr1)
                arr2 = n.moveDown(index_of_0)
                if (arr2!=None):
                    self.solveDFS(visited, arr2)
                arr3 = n.moveRight(index_of_0)
                if (arr3!=None):
                    self.solveDFS(visited, arr3)
#invoke solve1 method if you want to use DFS approach
    def solve1 (self):
        print(str(datetime.now()))
        self.solveDFS ( [], self.arr)
        print(str(datetime.now()))

class State:
    def __init__(self, arr, parent):
        self.arr    = arr
        self.parent = parent
        self.goal   = [1,2,3,8,0,4,7,6,5]
        self.weight = 0
        self.action = ""
        self.depth  = 0

    def setArr(self, arr):
        self.arr = arr

    def moveUp(self, index_of_0):
        if index_of_0 in [3,4,5,6,7,8]:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 - 3] = new_state[index_of_0 - 3], new_state[index_of_0]
            return new_state
        return None
    def moveRight(self, index_of_0):
        if index_of_0 in [0,1,3,4,6,7]:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 + 1] = new_state[index_of_0 + 1], new_state[index_of_0]
            return new_state
        return None
    def moveDown(self, index_of_0):
        if index_of_0 in [1,2,4,5,7,8]:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 - 1] = new_state[index_of_0 - 1], new_state[index_of_0]
            return new_state
        return None

    def moveLeft(self, index_of_0):
        if index_of_0 in [0,1,2,3,4,5]:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 + 3] = new_state[index_of_0 + 3], new_state[index_of_0]
            return new_state
        return None
    def createSuccessors (self, successors_heap, visited):
        index_of_0 = self.arr.index(0);
       # successors_heap = []
             if index_of_0 in [3,4,5,6,7,8]:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 - 3] = new_state[index_of_0 - 3], new_state[index_of_0]
#            heapq.heappush(successors_heap, new_state)
            if (not new_state in visited):
                successors_heap.put(new_state)

        if index_of_0 in [0,1,3,4,6,7]:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 + 1] = new_state[index_of_0 + 1], new_state[index_of_0]
            #heapq.heappush(successors_heap, new_state)
            if (not new_state in visited):
                successors_heap.put(new_state)

        if index_of_0 in [1,2,4,5,7,8]:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 - 1] = new_state[index_of_0 - 1], new_state[index_of_0]
            if (not new_state in visited):
                successors_heap.put(new_state)

        if index_of_0 in [0,1,2,3,4,5]:
            new_state = self.arr[:]
            new_state[index_of_0], new_state[index_of_0 + 3] = new_state[index_of_0 + 3], new_state[index_of_0]
            if (not new_state in visited):
                successors_heap.put(new_state)

        return successors_heap

state = range(9)
#my_puzzle = Puzzle([1,2,3,0,4,8,7,6,5])
my_puzzle = Puzzle([1,2,3,8,4,0,7,6,5])
my_puzzle.solve1()  
       
