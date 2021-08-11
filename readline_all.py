'''f=open("C:/source/새파일.txt", 'r')
while True:
    line = f.readline()
    if not line: break
    print(line)
f.close()
'''

'''
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

'''

'''
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1) + int(input2)
print("두 수의 합은 %s 입니다" % total)
'''
'''
print("you" "need" "python")
print("you"+"need"+"python")
print("you","need","python")
print("".join(["you","need","python"]))
'''
'''
f1=open("test.txt", 'w')
f1.write("Life is too short")
f1.close()

f2 = open("test.txt", 'r')
print(f2.read())
f2.close()
'''
'''
user_input = input("저장할 내용을 입력하세요:")
f = open('test.txt', 'a')   
f.write(user_input)
f.write("\n")               
f.close()
'''

f = open('test.txt', 'r')
body = f.read()
f.close()

body = body.replace('java', 'python')

f = open('test.txt', 'w')
f.write(body)
f.close()





