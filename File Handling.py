def show_file_data(file_path):
   """Displays the contents of a file."""
   try:
       with open(file_path, 'r') as file:
           contents = file.read()
           print(contents)
   except FileNotFoundError:
       print("Error: File not found.")
   except PermissionError:
       print("Error: Permission denied.")
   except Exception as e:
       print(f"An unexpected error occurred: {e}")


file = open("file.txt",'w')
d = file.write(" this is my code")
file.close()

file = open("file.txt", 'a')
v= file.write("\nthis is me ")

file = open("file.txt" , "r")
print(file.read())



#write a programme  to creat a dynamic file system where perform all the operation form the user input#