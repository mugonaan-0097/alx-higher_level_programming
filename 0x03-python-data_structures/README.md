0x03-python-data_structures

0. Print a list of integers
Write a function that prints all integers of a list.

1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.

2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).

3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.

4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

5. Can you C me now?
Write a function that removes all characters c and C from a string.

6. Lists of lists = Matrix
Write a function that prints a matrix of integers.

7. Tuples addition
Write a function that adds 2 tuples.

8. More returns!
Write a function that returns a tuple with the length of a string and its first character.

9. Find the max
Write a function that finds the biggest integer of a list.

10. Only by 2
Write a function that finds all multiples of 2 in a list.

11. Delete at
Write a function that deletes the item at a specific position in a list.

12. Switch
Complete the source code in order to switch value of a and b
You can find the source code here
Your code should be inserted where the comment is (line 4)
Your program should be exactly 5 lines long

13. Linked list palindrome
Technical interview preparation:
You are not allowed to google anything
Whiteboard first
Write a function in C that checks if a singly linked list is a palindrome.
Prototype: int is_palindrome(listint_t **head);
Return: 0 if it is not a palindrome, 1 if it is a palindrome
An empty list is considered a palindrom

14. CPython #0: Python lists
Create a C function that prints some basic info about Python lists.
Prototype: void print_python_list_info(PyObject *p);
Format: see example
Python version: 3.4
Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
OS: Ubuntu 14.04 LTS
Start by reading:
listobject.h
object.h
Common Object Structures
List Objectse
