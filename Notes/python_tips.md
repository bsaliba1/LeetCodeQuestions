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
- Initializing Array:
    - Empty: `arr = []`
    - Initialize w/ values: `arr = [1, 2, 3]`
    - Initialize all zeroes: `arr = [0] * N # out = [0,0,0, ...]`
    - Initialize w/ pattern: `arr = [1,2,3] * N # out = [1,2,3,1,2,3,...]`

### Math
- Truncating: `//` operator is used for truncating divide
- Reverse Int: Reverse an int with a loop to % 10 and /10 (see problem 7)
- Max Int: `float("inf")`
- Min Int: `-float("inf")`
- Get sign of int: `[-1,1][x<0]`

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
- Equivalent Trees
```
    def checkSubTree(first: TreeNode, second: TreeNode):
        if first and second:
            return first.val == second.val and Solution().checkSubTree(first.left, second.right) and Solution().checkSubTree(first.right, second.left)
        return first == second
```
- Binary Search
```
# Returns index of target
def binarySearch(nums: List[int], target: int) -> int:
    return binarySearchHelper(nums, target, 0, len(nums)-1)

def binarySearchHelper(nums: List[int], target: int, begin, end) -> int:
    mid = begin+end//2
    if nums[mid] < target: return binarySearchHelper(nums,target, mid+1, end)
    if nums[mid] > target: return binarySearchHelper(nums,target, 0, mid)
    return mid
```
