from handle_input import Literal
import copy

#check a clause exists in KB
def inKB(listLiter, KB):
    for i in KB:
        if(len(i)!=len(listLiter)):
            continue
        count = 0
        for j in range(0,len(listLiter)):
            if(listLiter[j].sign==i[j].sign and listLiter[j].isPos == i[j].isPos):
                count+=1
        if count == len(listLiter):
            return True
    return False

#resolute 2 clause
def resolution(C1, C2):
    res = []
    sign = ''
    isbr = 0
    for i in range(0,len(C1)):
        for j in range(0,len(C2)):
            if (C1[i].sign == C2[j].sign and C1[i].isPos!= C2[j].isPos):
                sign = C1[i].sign
                isbr  = 1
                break
        if isbr:
            break
    
    if sign == '':
        return False, []

    i = 0
    j = 0
    while i<len(C1) or j <len(C2):
        if i == len(C1):
            for k in range(j, len(C2)):
                if(C2[k].sign!=sign):
                    res.append(C2[k])
                    j=len(C2)
            break
        elif j == len(C2):
            for k in range(i, len(C1)):
                if C1[k].sign!= sign:
                    res.append(C1[k])
                    i=len(C1)
            break

        if(C1[i].sign < C2[j].sign):
            if(C1[i].sign != sign):
                res.append(C1[i])
            i+=1
        elif (C1[i].sign > C2[j].sign):
            if(C2[j].sign != sign):
                res.append(C2[j])
            j+=1
        elif (C1[i].sign == C2[j].sign and C1[i].sign == sign):
            i+=1
            j+=1
        else:
            if C1[i].isPos != C2[j].isPos:
                return -1, []
            else: 
                res.append(Literal(C1[i].isPos, C1[i].sign))
                i+=1
                j+=1

    return True, res
          

#Robinson algorithm
def Robinson(out_filename, KB, alpha):
    f = open(out_filename,'w')
    new = []
    for i in alpha:
        KB.append([i])
    
    while(True):
        count  = 0
        tmpKB = copy.copy(KB)
        str = ''
        isReturn = 0
        for i in range(0, len(tmpKB)-1):
            for j in range(i+1, len(tmpKB)):
                isRes, res = resolution(tmpKB[i],tmpKB[j])
                if isRes==1 and len(res)!=0 and not(inKB(res,KB)):
                    KB.append(res)
                    for k in range(0,len(res)):
                        if res[k].isPos == 0:    
                            if(k==0):
                                str = str + '-' + res[k].sign
                            else:    
                                str = str + ' OR -' + res[k].sign     
                        else:
                            if(k==0):
                                str = str  + res[k].sign
                            else:    
                                str = str + ' OR ' + res[k].sign     
                    str+='\n'
                    #print(str)
                    count +=1
                        
                elif isRes==1 and len(res)==0:
                    #print(tmpKB[i][0].printLiter())
                    #print(tmpKB[j][0].printLiter())
                    f.write("{}".format(count+1) + '\n')
                    f.write(str)
                    f.write('{}\n')
                    f.close()
                    isReturn = 1
            if isReturn:
                return True
                
        f.write("{}".format(count) + '\n')
        f.write(str)
        if(count == 0):
            f.close()
            return False
        
