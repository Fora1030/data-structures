import time
lookup = [None] *(1000)
def fib(n):
    if n <=1:
        return 1
    return fib(n-1) + fib(n-2)

def dyna_fib(n):
    """
    Dynamic programming fibonacci 
    --- 
        For the dynamic approach for this problem the efficiency increases are impressive.
        Once a fibonacci number (n) is computed it is saved in a list. Then when the next fibonacci
        number is computed (n+1) instead of recursively computing the number, the number in the n index
        of the list is returned. 
        

    Args:
        n (int): nth fibonacci number

    Returns:
        int: fibonacci number
    """
    if n == 0:
        return 0
    if n == 1: 
        return 1
    if lookup[n] is not None:
        return lookup[n]
    
    lookup[n] = dyna_fib(n-1) + dyna_fib(n-2)
    return lookup[n]


start_t = time.time()
for i in range(50):
    print(dyna_fib(i) ,end="\t")
end_t = time.time()
print('\n',end_t-start_t)

start_t = time.time()
for i in range(50):
    print(fib(i) ,end="\t")
end_t = time.time()
print('\n',end_t-start_t)