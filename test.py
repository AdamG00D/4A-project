name = 'adam-ghanem'
name2= 'adam_ghanem'
name3= 'Adam1ghanem'

def check_username(name):
    file = open('registration\\allowed.txt','r')
    
    chars = file.read()
    for char in name:
        if char not in chars:
            return False

    
    

    



print(check_username(name))
print(check_username(name2))
print(check_username(name3))
