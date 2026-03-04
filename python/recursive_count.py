
def recursiveCount(num = 0):
    # print(num)
    # num += 1
    # if num < 10:
    #     recursiveCount(num)
    if num == 10:
        return
    print(num)
    recursiveCount(num + 1)

'''
    Interview note

    For something simple like counting, recursion is not practical, but the 
    goal is to learn the recursion pattern.

    Most recursion interview problems follow this structure:

    1. Base case
    2. Do work
    3. Recursive call
'''