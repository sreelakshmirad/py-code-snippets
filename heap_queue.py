
import heapq

# 1. heapify
# 2. heappush
# 3. heappop
# 4.heappushpop
# 5.heapreplace
# 6.nlargest
# 7.nsmallest
 



li = [5, 7, 9, 1, 3]


# heapify
heapq.heapify(li)
print ("The created heap is:")
print (li)



# heappush
heapq.heappush(li,4)
print ("The modified heap after push")
print (li)


# heappop
print ("The popped and smallest element is : ")
print (heapq.heappop(li))
print (li)


# heappushpop
print ("The popped item using heappushpop() is : ")
print (heapq.heappushpop(li, 6))
print (li)


# heapreplace
print ("The popped item using heapreplace() is : ")
print (heapq.heapreplace(li, 2))
print (li)


# nlargest
print("The 3 largest numbers in list are : ")
print(heapq.nlargest(3, li))


# nsmallest
print("The 3 largest numbers in list are : ")
print(heapq.nsmallest(3, li))