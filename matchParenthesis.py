#With stack

def matchParanthesis(mylist):
    opening = ["(","{","["]
    closing = [")","}","]"]
    mystack = []
               
    for i in range(len(mylist)):
        if mylist[i] in opening:
            mystack.append(mylist[i])
            
        elif mylist[i] in closing:
            if mystack:
                popped = mystack.pop()
                if popped == "(" and mylist[i] != ")":
                    print("not matching")
                    return False
                if popped == "{" and mylist[i] != "}":
                    print("not matching")
                    return False
                if popped == "[" and mylist[i] != "]":
                    print("not matching")
                    return False
                
            else:
                print("not matching")
                return False
                
                
    if len(mystack)== 0:
        print("matching")
        return True
    else:
        print("not matching")
        return False

#With dictionary

def matchParanthesisDict(mylist):

    pairs = {")":"(",
             "}":"{",
             "]":"["}
    
    opening = set(pairs.values())
    
    mystack = []
               
    for char in mylist:
        if char in opening:
            mystack.append(char)
            
        elif char in pairs:
            if not mystack or mystack.pop() != pairs[char]:
                print("not maching")
                return False

                
    if len(mystack)== 0:
        print("matching")
        return True
    else:
        print("not matching")
        return False

            
matchParanthesis("({[]})")     #  matching
matchParanthesis("({[})")      #  not matching
matchParanthesis("((())")      #  not matching
matchParanthesis("{{}}")       #  matching
matchParanthesis("()[]{}")     #  matching
matchParanthesis("")           #  matching
        

matchParanthesisDict("({[]})")     #  matching
matchParanthesisDict("({[})")      #  not matching
matchParanthesisDict("((())")      #  not matching
matchParanthesisDict("{{}}")       #  matching
matchParanthesisDict("()[]{}")     #  matching
matchParanthesisDict("")           #  matching
