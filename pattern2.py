for i in range(1,5,1):
    print(' '*(4-i)+'*'*i)
    #OR
    # 1). print(' '*(4-i), end=' ')
    #     print('*'*i)
    #2). for i in range(1,5,1):
    #       print(' '*(4-i),'*'*i,sep='')
