#Time Complexity:: O(m*n)-all cells are visited once
#Space Complexity:: O(m*n)-each element in the grid has rotten oranges
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        coursesStudied = 0
        q = deque() 
        indegree = [0]*numCourses #indegree to store the number of prerequisites for each course
        adj = defaultdict(list) #adjacency matrix to store each courses, dependant courses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course) #changing course and its prereq, to each prereq course and its dependent courses
            indegree[course] += 1 #incrementing that number of prerequsite that course has
        
        for i in range(len(indegree)): #checking each course if it has any prerequisites
            if indegree[i]==0: #if every course has a prereq than no val in indegree array would be zero
                q.append(i) 
        
        if not q: #checking for cycle before starting(if q is empty since there is no zero's in indegree arr)
            return False 
        
        while q: #start when there is atleast 1 course with 0 prerequisites
            curr = q.popleft() #start with course that has zero prerequisites
            coursesStudied += 1 #count number of courses studied
            for dependent in adj[curr]: # find the courses that have current course has prerequisite
                indegree[dependent] -= 1 #update the prerequisites count as you complete the prerequist
                if indegree[dependent] == 0: #if all prerequisites complete
                    q.append(dependent) #then append course to q(course with no prereq)
                    
        if coursesStudied == numCourses: #if all courses completed then return True
            return True
        return False