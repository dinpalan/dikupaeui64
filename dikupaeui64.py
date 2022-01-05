from getmac import get_mac_address as ma

def dikupaeui64():
    print(f"your mac address is {ma()}")
    m = ma();
    #print(mac[1]);
    fm=m.split(':')
    #print(fm[0])
    #print(fm[0][0])
    #m=[1,8,2,3,4]
     
    if m[1] == 0 or m[1] == 1 or m[1] == 4 or m[1] == 5 or m[1] == 8 or m[1] == 9:
        #using eui-64 cheatsheet example c = e; 1 = 3;
        h = (2+m[1])
        if h == 10: 
            fm[0]=f'{fm[0][0]}''a'
            print(fm[0])
        #insert FFFE in between
            fm.insert(3,'ff')
            fm.insert(4,'fe')
            print("After applying eui-64 on mac address:")
            f=':'.join(fm)
            print(f)
        elif h == 11:
            fm[0]=f'{fm[0][0]}'"b"
            print(fm[0])
        #insert FFFE in between
            fm.insert(3,'ff')
            fm.insert(4,'fe')
            print("After applying eui-64 on mac address:")
            f=':'.join(fm)
            print(f)
        else:
            fm[0]=f'{fm[0][0]}{h}'
            print(fm[0])
        #insert FFFE in between
            fm.insert(3,'ff')
            fm.insert(4,'fe')
            print("After applying eui-64 on mac address:")
            f=':'.join(fm)
            print(f)
        
    if m[1] == 2 or m[1] == 3 or m[1] == 6 or m[1] == 7:
        #using eui-64 cheatsheet example c = e; 1 = 3;
        fm[0]=f'{fm[0][0]}{(m[1]-2)}'
        #print(fm)
        #insert FFFE in between
        fm.insert(3,'ff')
        fm.insert(4,'fe')
        print("After applying eui-64 on mac address:")
        f=':'.join(fm)
        print(f)

    #l = [10,11,'d',]

    
    
        
def main():    
    dikupaeui64();

if __name__=='__main__':
    main()
