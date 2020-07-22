# Ruby Notes

## Basics
### Data Types:
- Ranges
    - upper and lower bounds are inclusive unlike python
    - init: `x = 1..7`
    - iterate: 
    ```
    x.each do |i|
        [code]
    end
    ```
    - reverse iterate:
    ```
    x.reverse_each do |i|
    [code]
    end
    ```
### Printing:
- `puts` is similar to print – calling `to_s` – but adds a newline to the output
- `p` is similar to puts in that it adds a newline, but rather than calling `to_s`, p calls inspect.
### Declarations:
### Operators:
- Ternary: `condition ? if_true : if_false` 
- Exponent: `2**3 # 8`
- Chaining:
```
x = y = 2
x *= y *= 2
# x = 8, y = 4
```
### Command Line Args
### Lambdas
### Initializing Multiple Vals:
- different values: `x, y = 1, 2`
- same values: `x = y = 1` 
### Conversions:
### Assertions:
## Topics
### Math
### Strings
### Data Structures

#### HashMap:
#### Array:
- init with zeroes: `arr = [0]*length #length is size you want`
- **Map**
- **Reduce**
- **Filter**
#### Stack:
#### Trees
#### Heaps
