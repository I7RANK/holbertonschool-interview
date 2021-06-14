# 0x08. Palindrome integer
[Link to the project](https://intranet.hbtn.io/projects/444)

## Task
Write a function that checks whether or not a given unsigned integer is a palindrome.
<ul>
<li>Prototype: <code>int is_palindrome(unsigned long n);</code></li>
<li>Where <code>n</code> is the number to be checked</li>
<li>Your function must return <code>1</code> if <code>n</code> is a palindrome, and <code>0</code> otherwise</li>
<li>You are <strong>not allowed</strong> to allocate memory dynamically (malloc, calloc, …)</li>
</ul>

## Compilation
<li>compile with <code>gcc 4.8.4</code> using the flags <code>-Wall</code> <code>-Werror</code> <code>-Wextra</code> <code>and -pedantic</code></li>
</br>  

**command to compile**
<code>gcc -Wall -Wextra -Werror -pedantic -g3 -o palindrome 0-main.c 0-is_palindrome.c</code>
  
**and run with**
<code>./palindrome <number_to_check></code>
