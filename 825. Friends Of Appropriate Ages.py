from collections import Counter

class Solution:
    def numFriendRequests(self, ages: list[int]) -> int:
        invites = 0
        ages.sort()
        ages_dict = Counter(ages)
        for x in ages_dict.keys():
            for y in ages_dict.keys():
                #invites x->y
                if y > x or y <=0.5*x+7:
                    pass
                else:
                    if y == x:
                        invites += (ages_dict[x]-1)*(ages_dict[y])
                    else:
                        invites += (ages_dict[x])*(ages_dict[y])
                
        return invites


test_ages = [[20,30,100,110,120],[16,17,18],[16,16]]#, long_ages]
corr = [3,2,2]
test = Solution()
for i in range(len(test_ages)):
    print(test.numFriendRequests(test_ages[i]), test.numFriendRequests(test_ages[i])==corr[i])