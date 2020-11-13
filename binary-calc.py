# binary to interger calculator

print('** WELCOME TO BI_CALCULATOR **')

x = input("please enter your binary number : ")

your_length = x.__len__()

if (your_length % 4 == 0) :
    
    num_len = x.__len__()
    our_num = int(x)
    vartual_array = []

    for y in range(num_len):
        if y==0 :
            vartual_array.append(1)
        else:
            vartual_array.append(vartual_array[y-1]*2 )
            
    the_number = 0
    for y in range(num_len):
       
        if x[num_len-(y+1)] == "0":
            the_number = the_number + 0
        elif x[num_len-(y+1)] == "1":
            the_number = the_number + (vartual_array[y])
        else :
            print("INVALID BINARY NUMBER")
            break
    print("The interger value for " + x + " is : " + the_number.__str__())

else:
    print('Your binary number is not valid')

# this is just a comment to illusrate git usage