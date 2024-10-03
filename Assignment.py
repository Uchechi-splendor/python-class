# (1) How do you declare a variable in Python? Provide an example.
# answer: a varible is declared by assigning a value to it either as container or name

# example: #string
# countries='Paris'
# print(countries)
# print(type(countries))


# (2)What are the rules for naming variables in Python?
#     answer: Case-Sensitive
# Snake Case: Words are separated by underscores.
# Example: number_of_college_graduates
# Single or Double Quotes?
# String variables can be declared either by using single or double quotes:

# (3) What are the basic data types in Python? Give examples of each.
# x = "Hello World"	str	
# x = 20	int	
# x = 20.5	float	
# x = 1j	complex	
# x = ["apple", "banana", "cherry"]	list	
# x = ("apple", "banana", "cherry")	tuple	
# x = range(6)	range	
# x = {"name" : "John", "age" : 36}	dict	
# x = {"apple", "banana", "cherry"}	set	
# x = frozenset({"apple", "banana", "cherry"})	frozenset	
# x = True	bool	
# x = b"Hello"	bytes	
# x = bytearray(5)	bytearray	
# x = memoryview(bytes(5))	memoryview	
# x = None	NoneType

# (4)How do you convert one data type to another in Python? Provide an example.
#         How to Change Data Type in Python: A Step-by-Step Guide
#         Whether you are working with integers, floats, strings, or booleans, changing data types in Python involves a series of simple steps:
# How_do_you_convert_one_data_type_to_another_in_Python = ("Identify the source data type and the desired target data type for the variable",
#                                                          "Determine if an implicit or explicit conversion is most appropriate for the situation.",
#                                                          "Use the appropriate built-in function to perform the explicit type conversion or rely on Python's implicit conversion capabilities.",
#                                                          "Check for potential errors or loss of data during the conversion process.#Verify the successful conversion by analysing the type and value of the converted variable.")
# print(How_do_you_convert_one_data_type_to_another_in_Python)

#  #Changing integer to float
# num1 = 10
# num1_float = float(num1)
# print(type(num1_float))

#  #Changing float to integer
# num2 = 2.5
# num2_int = int(num2)
# print(type(num2_int))

#  #Changing integer to string
# num3 = 7
# num3_str = str(num3)
# print(type(num3_str))

#  #Changing string to boolean
# str1 = "Hello"
# str1_bool = bool(str1)
# print(type(str1_bool))

# #(5) What is type conversion in Python? 
# Type_conversion = "is the process of converting data of one type to another. For example: converting int data to str."
# #There are two types of type conversion in Python.
# #Implicit Conversion - automatic type conversion
# #Explicit Conversion - manual type conversion
# Why_is_it_necessary = "It helps us do operations on values having different data types. For example: concatenating an integer to a string."
# #Example
# float_string = '78.7'
# print(float_string)
# print(type(float_string))
# converted = float(float_string)
# print(converted)
# print(type(converted))
# new_int = int(converted)
# print(new_int)

# #(6)Describe the difference between implicit and explicit type conversion in Python.
#implicit type conversion is automatically performed by the compiler when differing data types are intermixed in an expression.
# This is performed without programmers intervention
#Explicit type conversion is user-defined conversion that forces a n expression to be of specific type
# implicit_type_conversion = "is performed by a Python interpreter only." 
# Explicit_type_conversion = "is performed by the user by explicitly using type conversion functions in the program code."
# #e.g
# Example = "implicitly converts the value of k to a single-precision floating-point value before assigning it to q."
# Explicit_example = "Int keyword converts the value of q back to an integer before assigning it to k."

# #(7)What is the purpose of using comments in Python? Give an example.
# comments = 'Comments in Python are used to explain the purpose of the code, make it more readable,\n and provide additional information for developers. Commented codes do not\n show when it/''s printed or executed.'
# print(comments)

# #"Hello, world"
# print("Hello, world")

# Concept_of_dynamic_typing = "Dynamic typing in Python refers to the ability of the language to determine the type of\n variable at runtime, without the need of explicit type declarations, i.e Python automatically assigns\n the appropriate type based on the value assigned to the variable."
# print(Concept_of_dynamic_typing)

# Implications= 'Flexiblity, Simplicity, Potential for errors, Readablity'
# print(Implications)

# output_checkout = "In Python, you can check the data type of a variable using the, type() function."
# print(output_checkout)

# Built_in_functions = 'int(): converts a value to an integer\n  2. float(): Converts a value to a floating-point number.\n  3. str(): Converts a value to a string.\n  4. bool(): Converts a value to a boolean.'
# print(Built_in_functions)

# #(11) Discuss the significance of using meaningful variable names in Python programming. Provide an example.
# Readability = "Meaningful variable names make your code more readable and understandable to yourself and other developers. Clear variable names convey the purpose and intent of the variable, making it easier to follow the logic of the code."
# Maintainability = "When you revisit your code in the future or collaborate with other developers, descriptive variable names help you understand the code's functionality without having to decipher each variable's purpose."
# Documentation = "Well-named variables serve as self-documentation, reducing the need for excessive comments to explain the purpose of each variable."
# Reduced_Errors = "Clear variable names can help prevent errors and misunderstandings by providing context for the values stored in the variables."
