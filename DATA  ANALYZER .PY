print("Welcome to  the Data Analyzer and Transfomer Program")
print("==================Main Menu=========================")
while True:
 print("1.Input Data")
 print("2.Display Data Summary(Build-in functions)")
 print("3.Calculate Factorial (Recursion)")
 print("4.Filter Data by Threshold(lambda function)")
 print("5.Sort Data")
 print("6.Display Dataset statistics(return multiple values)")
 print("7.Exit Program")

 choice=int(input("please enter your choice: "))

 if choice==1:
  Data=[]
  Data=input("enter data for 1D array(separated by spaces):")
  arr=list(map(int,Data.split()))
  print(arr)
  print("Data has been stored successfully")

 elif choice==2:
  print("======Display Data Summary=========")
  print("-Total Element: ",len(arr)) 
  print("-Minimum value: ",min(arr))
  print("-maximum value: ",max(arr))
  print("-sum of all values: ",sum(arr))
  print("-average value: ",sum(arr)/len(arr))

 elif choice==3:
  def factorial(n):
   """This function work to calculate factorial using recusion """
   if n==0 or n==1:
    return 1
   return n*factorial(n-1)
  num=int(input("Enter a number to calculate a factorial")) 
  print(f'factorial of {num} is {factorial(num)}')
  print(factorial.__doc__)

 elif choice==4:
  thresold=int(input("Enter a thresold Value to filter out data above this value"))
  filtered_value=list(filter(lambda x:x>thresold,arr )) 
  print(filtered_value)

 elif choice==5:
  print("1.Ascending order")
  print("2.Descending order")
  sort_choice=int(input("Enter your choice: "))
  if sort_choice==1:
   sorted_arr=sorted(arr)
   print("Sorted Data in Ascending order: ",sorted_arr)
  elif sort_choice==2:
   sorted_arr=sorted(arr,reverse=True)
   print(sorted_arr)
   print("Sorted Data in Descending order: ",sorted_arr)

 elif choice==6:

    def statistics(Data):
        """This function returns minimum, maximum, total and average."""

        minimum = min(Data)
        maximum = max(Data)
        total = sum(Data)
        average = total / len(Data)

        return minimum, maximum, total, average

    minimum, maximum, total, average = statistics(arr)

    print("----- Dataset Statistics -----")
    print("- Minimum Value :", minimum)
    print("- Maximum Value :", maximum)
    print("- Sum of all Values :", total)
    print("- Average Value :", average)

    print(statistics.__doc__)

 elif choice==7:
  print("Thank you for using the Data analyzer and Transformer Program")
  break
  

