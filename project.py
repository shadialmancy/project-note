print("----------Note----------")
end = True
dict={}
while end:
    x=input("Would you like to:\n1-Create\n2-Edit\n3-Delete\n4-Display")
    
    x=x.lower()

    if x=="create":
        name=input("enter the note name:")
        if name in dict:
         note=input("enter the note:")
         dict[name]=note
        else:
                        print("name already used")
    elif x=="edit":
        name=input("enter the note name:")
        if name in dict:
         note=input("enter the new note")
         dict[name]=note
        else:
                        print("note name not found")
    elif x=="delete":
                    name=input("enter the note name:")
                    if name in dict:
                                    dict.pop(name)
                    else:
                                    print("note name not found")
                    
    elif x=="display":
        
            print(dict)
    else:
        print("Error: Input Undefined")
    end=input("Would you like to contuine?\nTrue/False")
    if end == True:
                    continue
    else:
                    break
                
