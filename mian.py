import hashlib



def main():
    sha1 = input("The SHA1 To Crack : ")
    cleaned_sha1 = sha1.strip().lower()
    with open('./rockyou.txt') as passwods:
        for line in passwods:
            passwod = line.strip()
            passwod_sha1 = hashlib.sha1( passwod.encode() ).hexdigest()
            if cleaned_sha1 == passwod_sha1:
                print("The password is : ", passwod)
                return
            
        


    



if __name__ == '__main__':
    main()