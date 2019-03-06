def ruler(number):
    if type(number) == int:
        for i in [int(x/10) for x in range(1,number+1) if x%10 == 0]:
            print((10-len(str(i))%10) * ' ',end ="")
            print(i,end = "")
        print('\n',end="")
        for j in range(1,number+1):
            if j%10 != 0:
                print(j%10,end ="")
            else:
                print(0, end="")
        print('\n', end="")
    else:
        print("Only number as a parameter allowed.")

if __name__ == '__main__':
    ruler(5)
    ruler(10)
    ruler(25)
    ruler(51)
    ruler(80)
    ruler(151)

