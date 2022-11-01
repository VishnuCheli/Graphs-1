#Time Complexity:: O(n)-all persons in trust list are visited
#Space Complexity:: O(n)-indegree list is used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """

        indegree = [0] * n #create an indegree array and store the count of each persons dependents

        for person, trusted_person in trust: #each person and they're trusted persons indegree value updated
            indegree[person-1]-=1
            indegree[trusted_person-1]+=1

        for i in range(len(indegree)): # return the indegeree of the town judge who doesn't trust anyone
            if indegree[i] == n-1:
                return i+1

        return -1