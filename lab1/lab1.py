
def max_list_iter(int_list) -> int:  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError('List must not be None!')
   if len(int_list) == 0:
      return None
   
   cur_max = int_list[0]
   for num in int_list[1:]:
      if num > cur_max:
         cur_max = num
   return cur_max

def reverse_rec(int_list) -> list:   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list is None:
      raise ValueError('List must not be None')
   
   if len(int_list) == 0:
      return []
   elif len(int_list) == 1:
      return int_list
   else:
      reversed_sublist = reverse_rec(int_list[1:])
      reversed_sublist.append(int_list[0])
      return reversed_sublist

def bin_search(target, low, high, int_list) -> int:  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if target is None or int_list is None:
      raise ValueError('target and int_list must not be None')
   if len(int_list) == 0:
      return None
   if low > high:
      return None  # target is not present in list

   mid = (low + high) // 2
   if target == int_list[mid]:
      return mid
   elif target < int_list[mid]:
      return bin_search(target, low=low, high = mid-1, int_list = int_list)
   else:  # target > int_list[mid] 
      return bin_search(target, low = mid + 1, high = high, int_list = int_list)

def reverse_list_mutate(int_list) -> None:
   '''Reverses a list, modifies the input list, returns None
   If list is None, raises ValueError'''
   if int_list is None:
      raise ValueError("int_list must not be None")
   if len(int_list) == 0:
      return  # do nothing to an empty list

   low: int = 0
   high: int = len(int_list) - 1
   while low < high:
      int_list[low], int_list[high] = int_list[high], int_list[low]
      low += 1
      high -= 1