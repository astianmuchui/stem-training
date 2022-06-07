# Assignment 
"""
For range of integers between o and n: 
If the number is an even number, half it. 
If the number is an odd number, square it.
For the output generated in the previous step, Write the result to a file and name it result.txt.

"""

def intAnalyzer(n):
    doc = open("result.txt","x")
    file = open("result.txt","w")
    n = int(n)
    for i in range(n):
        if i%2 ==0:

            b = i/2
            file.write(f"{b} \n")
        else:
            c = i*2
            file.write(f"{c} \n")
            


    file.close()
intAnalyzer(10)