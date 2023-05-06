# # import time

# # while True:
# #     try:
# #         num = int(input("""what size?
# #         => """))
# #     except:
# #         print("Enter a number again, please!")
# #         continue
# #     else:
# #         break

# # time.sleep(0.3)

# # print(f'size = {num} x {num}')

# # for i in range(0,num):
# #     for j in range(0,num):
# #         print("[_]",end='')
# #     print("\n")

# size=int(input('what size =  '))
# for x in range(0,size): 
#     for y in range(0,size):
#         if y == x:
#             print(" ❌ ", end="")
#         elif y==size-x-1:
#              print(" ❌ ",end="")
#         else:
#              print(" ⬜ ",end="")
#     print("\n")

#=======================================================================================

# num=input('write\n')
# y=0
# last=0
# for x in num:
#     if x=='i':
#         y+=1
#         last='i'
#     elif x=='v':
#         y+=5
#         if last=='i':
#             y-=2
#         last='v'
#     elif x=='x':
#         y+=10
#         if last=='i':
#             y-=2
#         last='x'
#     elif x=='l':
#         y+=50
#         last='l'
#     elif x=='c':
#         y+=100
#         last='c'
#     elif x=='d':
#         y+=500
#         last='d'
#     elif x=='m':
#         y+=1000
#         last='m'
#     else:
#         print('do again')
# print(y)

#===========================================================================================

num=[2,1,2,0,3,1,2]

m=0
max_pos=0
lmax=0
rmax=0
size=0
total=0
size=len(num)

for x,i in enumerate(num):
    if i> m:
        m=i
        max_pos=x

for x,i in enumerate(num):
    if 0<=x<max_pos:
        if i > lmax:
            lmax=i 

for x,i in enumerate(num):
    if size>x>max_pos:
        if i>rmax:
            rmax=i

for x,i in enumerate(num):
    if 0<x<max_pos:
        if i < lmax:
            total += lmax - i

for x,i in enumerate(num):
    if size>x>max_pos:
        if i < rmax:
            total += rmax - i



print(total)