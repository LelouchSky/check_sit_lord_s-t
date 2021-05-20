sentence = '*i love python'
        

if sentence[0].startswith('*'):
    
    sentence = sentence.rsplit(sep = ' ')
    print(sentence)# ['*i', 'love', 'python']
    # 以空格为停顿点，把string化为list

    # sentence[0] = list(sentence[0])
    # sentence[0].pop(0)
    
    # sentence[0] = list(sentence[0]).pop(-1)
    # 把pop(-1)的值赋给了sentence[0]
    sentence[0] = sentence[0][1:]
    print(sentence[0])
    sentence[0] = ''.join(sentence[0])
    
    for index in range(0,len(sentence)):
        words = sentence[index]
        words = words.capitalize()
        words = list(words)
        words[-1] = words[-1].upper()
        words = ''.join(words)
        sentence[index] = words
    sentence = ' '.join(sentence)

else:
    sentence = list(sentence)
    sentence_list = []
        
    for index in range(0,len(sentence)):
        space = sentence[index]
        if space == ' ':
            space = ','
            if index+1 < len(sentence) and sentence[i+1] == ' ':
                 continue
        sentence_list.append(space)

    if sentence_list[-1] == ',':
        sentence_list.pop()    

    sentence = ''.join(sentence_list)
            
    

print(sentence)