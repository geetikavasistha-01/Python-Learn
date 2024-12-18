def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
# return means that the function is returned now the code below that will not run
        
    except Exception as e:
        print(e) 
        return


    finally:
        print("Hey I am inside of finally")


main()