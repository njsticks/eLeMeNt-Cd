stock = {}
database = {}
 
for i in range(100):

    option = int(input("Press 00 to Add Stock to your Database, or Press 99 to View Database: "))

    if option == 00:

        print("\n")
        
        stocklmt = int(input("Choose Stock Item(s): "))


        if stocklmt == 1:

            print("\n")        
            add = input("Enter Your Stock: ")
            add_ = int(input("Enter Your Stock Number: "))
            total = {add: add_}
            stock.update(total)
            file = open("SaveData.txt", "a+")
            file.write(str(stock))
            file = open("SaveData.txt", "r")
            file2 = open("SaveData.txt", "r")
            print("Item(s) is Added to the Database")
            
        elif stocklmt == 2:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = (open("SaveData.txt", "r"))
                print("Item(s) is Added to the Database")
            
        elif stocklmt == 3:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print("Item(s) is Added to the Database")
                
        elif stocklmt == 4:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print("Item(s) is Added to the Database")
                
        elif stocklmt == 5:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print("Item(s) is Added to the Database")
                
        elif stocklmt == 6:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print("Item(s) is Added to the Database")
                
        elif stocklmt == 7:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                add6 = input("Enter Your Stock: ")
                add_6 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5, add6: add_6}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print("Item(s) is Added to the Database")
                
        elif stocklmt == 8:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                add6 = input("Enter Your Stock: ")
                add_6 = int(input("Enter Your Stock Number: "))
                add7 = input("Enter Your Stock: ")
                add_7 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5, add6: add_6, add7: add_7}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print("Item(s) is Added to the Database")
                
        elif stocklmt == 9:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                add6 = input("Enter Your Stock: ")
                add_6 = int(input("Enter Your Stock Number: "))
                add7 = input("Enter Your Stock: ")
                add_7 = int(input("Enter Your Stock Number: "))
                add8 = input("Enter Your Stock: ")
                add_8 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5, add6: add_6, add7: add_7, add8: add_8}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print("Item(s) is Added to the Database")
                
        elif stocklmt == 10:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                add6 = input("Enter Your Stock: ")
                add_6 = int(input("Enter Your Stock Number: "))
                add7 = input("Enter Your Stock: ")
                add_7 = int(input("Enter Your Stock Number: "))
                add8 = input("Enter Your Stock: ")
                add_8 = int(input("Enter Your Stock Number: "))
                add9 = input("Enter Your Stock: ")
                add_9 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5, add6: add_6, add7: add_7,  add8: add_8, add9: add_9}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print("Item(s) is Added to the Database")

        elif option == 99:

                print("\n")
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())

        else:
            print("\n")  
            print("Invalid Prompt, Restart the shell")

        option = int(input("Press 00 to Add Stock to your Database, or Press 99 to View Database: "))

        if option == 00:

            print("\n")
            
            stocklmt = int(input("Choose Stock Item(s): "))


            if stocklmt == 1:

                print("\n")        
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                total = {add: add_}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
            
            elif stocklmt == 2:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
                print(file2.read())
            
            elif stocklmt == 3:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
                
            elif stocklmt == 4:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
                
            elif stocklmt == 5:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
                
            elif stocklmt == 6:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
                
            elif stocklmt == 7:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                add6 = input("Enter Your Stock: ")
                add_6 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5, add6: add_6}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
                
            elif stocklmt == 8:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                add6 = input("Enter Your Stock: ")
                add_6 = int(input("Enter Your Stock Number: "))
                add7 = input("Enter Your Stock: ")
                add_7 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5, add6: add_6, add7: add_7}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
                
            elif stocklmt == 9:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                add6 = input("Enter Your Stock: ")
                add_6 = int(input("Enter Your Stock Number: "))
                add7 = input("Enter Your Stock: ")
                add_7 = int(input("Enter Your Stock Number: "))
                add8 = input("Enter Your Stock: ")
                add_8 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5, add6: add_6, add7: add_7, add8: add_8}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())
                
            elif stocklmt == 10:
                print("\n")  
                add = input("Enter Your Stock: ")
                add_ = int(input("Enter Your Stock Number: "))
                add1 = input("Enter Your Stock: ")
                add_1 = int(input("Enter Your Stock Number: "))
                add2 = input("Enter Your Stock: ")
                add_2 = int(input("Enter Your Stock Number: "))
                add3 = input("Enter Your Stock: ")
                add_3 = int(input("Enter Your Stock Number: "))
                add4 = input("Enter Your Stock: ")
                add_4 = int(input("Enter Your Stock Number: "))
                add5 = input("Enter Your Stock: ")
                add_5 = int(input("Enter Your Stock Number: "))
                add6 = input("Enter Your Stock: ")
                add_6 = int(input("Enter Your Stock Number: "))
                add7 = input("Enter Your Stock: ")
                add_7 = int(input("Enter Your Stock Number: "))
                add8 = input("Enter Your Stock: ")
                add_8 = int(input("Enter Your Stock Number: "))
                add9 = input("Enter Your Stock: ")
                add_9 = int(input("Enter Your Stock Number: "))
                total = {add: add_, add1: add_1, add2: add_2, add3: add_3, add4: add_4, add5: add_5, add6: add_6, add7: add_7,  add8: add_8, add9: add_9}
                stock.update(total)
                file = open("SaveData.txt", "a+")
                file.write(str(stock))
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())

        elif option == 99:

                print("\n")
                file = open("SaveData.txt", "r")
                file2 = open("SaveData.txt", "r")
                print(file2.read())

    else:
        print("\n")  
        print("Invalid Prompt, Restart the shell")












     

           
