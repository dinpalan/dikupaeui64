from getmac import get_mac_address as ma

def dikupaeui64():
    print(f"your mac address is {ma()}")
    mac = ma();
    #print(mac[1]);
    fm=mac.split(':')
    #print(fm[0])
    #print(fm[0][0])
    if mac[1] == 'c':
        #using eui-64 cheatsheet example c = e; 1 = 3;
        fm[0]=f'{fm[0][0]}e'
        #print(fm)
        #insert FFFE in between
        fm.insert(3,'ff')
        fm.insert(4,'fe')
        print("After applying eui-64 on mac address:")
        f=':'.join(fm)
        print(f)
        
def main():    
    dikupaeui64();

if __name__=='__main__':
    main()
