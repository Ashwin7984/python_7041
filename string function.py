'''
string is a group of character .
string index start for 0.
python also provided also negative last character of string will continue -1
'''

s ="Tops Technology"

print(s)
print("length of String : ",len(s))
print(s.capitalize())
print(s.casefold())
print(s.center(30,"$"))
print(s.count("o"))
print(s.endswith("ogy"))
print(s.find("log"))
print(s.index("T"))
print("tops123".isalnum())
print("123".isalnum())
print("tops".isalnum())
print("tops 123".isalnum())
print("123".isnumeric())
print("tops".isalpha())
print(s.istitle())
print(" ".isspace())
print(s.upper())
