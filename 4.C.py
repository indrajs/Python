vowels=['A','E','I','O','U','a','e','i','o','u']
vow=[]
word=input("Enter the word:")
vow=[i for i in word if i in vowels]
print("the lis of vowels in the word are",vow)
