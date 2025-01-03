#to reverse and insert element at any index in list and remove and pop 


# to reverse the list using python
list=[1,2,3,4,5]
list.reverse()
print(list)


#to insert element in a list at any index 
list=[1,3,4,6,7]
list.insert(2, 99)
print(list)
# yha agar mne 99 ko index par rakha aur element par 2 to compiler will just append this value at last and values will be stored at 
# 6,7,8,9......index if we try to acess them then compiler will give index error


# to remove the element from the list 
list=[2,1,3,1]
list.remove(1)
print(list)


#to remove the element from particular index from the list 
list=[1,2,3,4,5]
list.pop(3)
print(list)