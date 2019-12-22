# Python Notes

## Basics
- Printing:
    - Print on same line: `print("...", end = '')` will prevent a \n character to be added to the end of your string
- Declarations:
    - Static Functions: `@staticmethod` can be used to declare the following function as static
    - Functions: `def func_name(var_name = default_val: var_type) -> output_type: ...`
    - Classes `class ClassName: `
- Operators:
    - Ternary: `condition_if_true if condition else condition_if_false`
    - Exponent: `2**3 == pow(2,3)`
- Conversion:
    - string -> int: `int(mystring)`
    - int -> string: `str(myint)`

## Topics

### Arrays
- HashMap: `dict()` is used liked a hashmap
    - use `in` keyword to check if key is contained in dict

### Math
- Truncating: `//` operator is used for truncating divide
- Reverse Int: Reverse an int with a loop to % 10 and /10 (see problem 7)
- Max Int: `float("inf")`
- Min Int: `-float("inf")`

### Strings
- Indexing:
    - `mystring[0]` will give you the first letter
    - `mystring[-1]` will give you the last element
- Slicing: (see example 7)
    - syntax - `mystring[first:last:step]` , note if step < 0 then step backwards
        - `mystring[::] == mystring[0:len(mystring)-1]`
        - `mystring[::-1]` reverses string
    - ex. `"abcdefg"[:0:-2]` outputs "gec"

### Trees
- Traversal
    - Post Order:
        ```
        def printPostorder(node: TreeNode):
            if node is None:
                return

            # first recur on left subtree
            printPostorder(node->left);

            # then recur on right subtree
            printPostorder(node->right);

            # now deal with the node
            print(node.data)
         ```

     - In Order:
        ```
        def printInorder(node: TreeNode):
            if node is None:
                return

            # first recur on left subtree
            printInorder(node->left);

            # then print the node data
            print(node.data)

            # now recur on right subtree
            printInorder(node->right);
        ```

      - Pre Order:
        ```
        def printPreorder(node: TreeNode):
            if node is None:
                return

            # first print the node data
            print(node.data)

            # then recur on left subtree
            printPreorder(node->left);

            # now recur on right subtree
            printPreorder(node->right);
        ```