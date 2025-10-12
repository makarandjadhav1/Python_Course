letter = '''      Dear <|Name|>, 
                You are selected! 
                <|Date|> '''
replace_String = letter.replace("<|Name|>","Makarand").replace("<|Date|>","10 Oct 2004")
print(replace_String)