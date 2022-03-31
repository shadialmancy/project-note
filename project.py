print("----------Note----------")
end = True
dict={}
while end:
    x=input("Would you like to:\n1-Create\n2-Edit\n3-Delete\n4-Display\n")
    
    x=x.lower()

    if x=="create":
        name=input("enter the note name:")
        if name in dict:
         print("name already used")
        else:
         note=input("enter the note:")
         dict[name]=note
                        
    elif x=="edit":
        name=input("enter the note name:")
        if name in dict:
         print("note name not found")   
         
        else:
         note=input("enter the new note")
         dict[name]=note               
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
    finish=input("Would you like to contuine?\nTrue/False").capitalize()
    
    if finish == "True":
                    continue
    else:
                    end=False
                
