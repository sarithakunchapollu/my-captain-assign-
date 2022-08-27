def most_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(most_frequency('saritha'))

Output:
{ 's' :  1,  'a' :  2,  'r' :  1,  'i' :  1,  't' :  1,  'h' :  1 }
