# defintion of a function
# def test_function():
#    print("obama prism")
# test_function()

# testing number of arguments
# def my_function(fname):
#  print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# arbitrary *args
# def my_function(*kids):
 # print ("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def fib(n):
#  """Print numbers in the fibonacci sequence up to n"""
#  a, b = 0, 1
#  while a < n:
#    print(a, end=' ')
#    a, b = b, a + b
#  print()

# fib(2000)

# returning data instead of printing
def fib2(n):
  result = []
  a, b = 0, 1
  while a < n:
    result.append(a)
    a, b = b, a + b
  return result

fib2(100)

# """returning values in a function"""
# def my_function(x):
#  return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

def tri_recursion(k): """ define tri_recusion argument """
  if(k > 0): # recurse if k is greater than 0
    result = k + tri_recursion(k - 1) # calls tri_recursion(k - 1) to get all numbers from 1 to k-1 -- i.e. the value of tri_recursion(1) =1 up to tri_recursion(k-1)
    print(result) # prints the stored value result in asending order as the call returns, since it is after the recursive call
  else:
    result = 0 # if k=0, then returns 0 and prints nothing
  return result # passes result from the base case to the function

print("Recursion Example Results:")
tri_recursion(6)
