def getstr(s):# excel中将字符串、数字、小数混用情况下转换成正常字符串，如数字123不会变成123.0，注意123.010还是123.01，只是保留位数不同而显示不同
    if not isinstance(s,str):
        if str(s)[-2:] == '.0':
            s = str(int(s))# 数字
        else:
            s = str(s)# 小数
    return s
            
