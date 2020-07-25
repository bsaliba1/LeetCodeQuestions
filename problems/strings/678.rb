# 678. Valid Parenthesis String
# Link: https://leetcode.com/problems/valid-parenthesis-string/

# Works but Too Slowly

# @param {String} s
# @return {Boolean}
def check_valid_string(s)
    trimmed = trim(s)
    if trimmed == ""
        return true
    end
    count = trimmed.count('*')
    if count == 0
        return false
    end
    
    s_map = stars_map(trimmed)
    substitute = trimmed.split('')
    i = 3**count    #00 01 02 10 11 12 20 21 22
    while i>0
        i_cp = i
        (0..count-1).each do |x|
            bit = i_cp%3
            i_cp/=3
            substitute[s_map[x]] = i_to_val(bit)
        end
        final = trim(substitute.join(''))
        if final == ""
            return true
        end

        i-= 1
    end
    return false
end

def trim(s)
    stack = []
    arr_format = s.split('')
    index = 0
    arr_format.each do |c|
        if c == '('
            stack.push([c,index])
        elsif c == ')'
            if not stack.empty?
                _,leftmost_i = stack.pop()
                arr_format[leftmost_i] = ''
                arr_format[index] = ''
            end
        end
        index+=1
    end
    return arr_format.join('')
end

def stars_map(s)
    s_map = []
    index = 0
    s.each_char do |c|
        if c == '*'
            s_map.push(index)
        end
        index+=1
    end
    return s_map
end

def i_to_val(i)
    if i == 0
        return '('
    elsif i == 1
        return ')'
    else
        return ''
    end
end
        
