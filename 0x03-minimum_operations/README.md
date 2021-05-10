# 0x03. Minimum Operations
[Link to the project](https://intranet.hbtn.io/projects/488)

## Algorithms description
In a text file, there is a single character <code>H</code>. Your text editor can execute only two operations in this file: <code>Copy All</code> and <code>Paste</code>. Given a number <code>n</code>, write a method that calculates the fewest number of operations needed to result in exactly <code>n H</code> characters in the file.

- Prototype: <code>def minOperations(n)</code>
- Returns an integer
- If <code>n</code> is impossible to achieve, <code>return 0</code>

### Example
<p><code>n = 9</code></p>
<p><code>H</code> -&gt; <code>Copy All</code> -&gt; <code>Paste</code> -&gt; <code>HH</code> -&gt; <code>Paste</code> -&gt;<code>HHH</code> -&gt; <code>Copy All</code> -&gt; <code>Paste</code> -&gt; <code>HHHHHH</code> -&gt; <code>Paste</code> -&gt; <code>HHHHHHHHH</code></p>

Number of operations: <code>6</code>
