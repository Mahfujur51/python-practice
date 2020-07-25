def moon(k):
    if (k>0):
        result=k+moon(k-1)
        print(result)
    else:
        result=0
    return result
print("\n\n Recursion example result")
moon(5)