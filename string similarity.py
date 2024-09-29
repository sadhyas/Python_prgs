import difflib
def stringsimilarity(str1, str2):
    result=difflib.SequenceMatcher(a=str1.lower(),b=str2.lower())
    return result.ratio()
str1=input("enter string 1: ")
str2=input("enter string 2: ")
print("original strings are:")
print(str1)
print(str2)
print("Similarity between the 2 strings is:",stringsimilarity(str1,str2))
