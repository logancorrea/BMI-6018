#%% the humble print statement
'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
'''

def wrong_add_function(arg1,arg2):
    
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
      arg1[arg1_index]=arg_2_sum  
      print(f"We are making an error in the loop. The correct answer:[2,3,4]; the given answer: {arg1}")
      arg1_index+=1
   return arg1

arg1 = [1,2,3]
arg2 = [1,1,1]

wrong_add_function(arg1, arg2)

'''
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''
    
def correct_add_function(arg1, arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1

arg1 = [1, 2, 3]
arg2 = [1, 1, 1]

correct_add_function(arg1, arg2)

#%% try, except
"""
2.b
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
returns an error message to the user, in case users give invalid inputs,
(for example an input of ["5","2", 5])
: "Your input argument [1 or 2] at element [n]
is not of the expected type. Please change this and rerun. Name this function 
exception_add_function()
"""
def wrong_add_function(arg1, arg2):
        #numeric section
       if sum([type(i)==int for i in arg1])==len(arg1) and \
          sum([type(i)==int for i in arg2])==len(arg2):
             arg1_index=0
             while arg1_index < len(arg1):
                arg_2_sum = 0
                for arg2_elements in arg2:
                   arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
                arg1[arg1_index]=arg_2_sum  
                arg1_index+=1
             return arg1
       #string section
       elif sum([type(i)==str for i in arg1])==len(arg1) and \
          sum([type(i)==str for i in arg2])==len(arg2):
             arg1_index=0
             while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                   arg_2_sum += arg2_elements
                arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
                arg1_index+=1
             return arg1
        
def exception_add_function(arg1, arg2):
    try:
        result = wrong_add_function(arg1, arg2)
        return result
    except TypeError:
        arg_index = arg1.index(arg2[0] if isinstance(arg2[0], str) else arg2[1])
        arg_number = "1" if isinstance(arg2[0], str) else "2"
        return f"Your input argument [{arg_number}] at element [{arg_index}] is not of the expected type. Please change this and rerun."

arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '1', 1]

exception_add_function(arg_str_1, arg_str_2)

'''
2.c
Without modifying the string section code itself or the input directly, 
write a try, except block that catches the issue with the input below and 
gets it to process via the string section. IE, do not, outside the function,
change the values of arg_str_1 or arg_str_2. Name this function 
correction_add_function(), i.e you will not be updating the wrong_add_function,
you will simply handle the error of wrong inputs in a seperate function, you want
the wrong_add_function to output its current result you are only bolstering the 
function for edge cases .
'''

def wrong_add_function(arg1, arg2):

       #numeric section
       if sum([type(i)==int for i in arg1])==len(arg1) and \
          sum([type(i)==int for i in arg2])==len(arg2):
             arg1_index=0
             while arg1_index < len(arg1):
                arg_2_sum = 0
                for arg2_elements in arg2:
                   arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
                arg1[arg1_index]=arg_2_sum  
                arg1_index+=1
             return arg1
        
       #string section
       elif sum([type(i)==str for i in arg1])==len(arg1) and \
          sum([type(i)==str for i in arg2])==len(arg2):
             arg1_index=0
             while arg1_index < len(arg1):
                arg_2_sum = ''
                for arg2_elements in arg2:
                   arg_2_sum += arg2_elements
                arg1[arg1_index]=arg1[arg1_index]+str(arg_2_sum)
                arg1_index+=1
             return arg1
        
def correction_add_function(arg1, arg2):
    try:
        result = wrong_add_function(arg1, arg2)
        return result
    except TypeError:
        new_arg1 = [str(item) for item in arg1]
        new_arg2 = [str(item) for item in arg2]
        return wrong_add_function(new_arg1, new_arg2)

arg_str_1 = ['1', '2', '3']
arg_str_2 = ['1', '1', 1]

wrong_add_function(arg_str_1, arg_str_2)