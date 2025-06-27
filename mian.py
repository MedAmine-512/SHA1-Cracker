import hashlib
import argparse
import os




def crack(sha1, wordlist):
    if not os.path.isfile(wordlist):
        print(f"[!] There is no file ")


    cleaned_sha1 = sha1.strip().lower()


    with open(wordlist) as passwods:
        for line in passwods:
            passwod = line.strip()
            passwod_sha1 = hashlib.sha1( passwod.encode() ).hexdigest()
            if cleaned_sha1 == passwod_sha1:
                print("[+] The password is : ", passwod)
                break




def main():

    parser = argparse.ArgumentParser(description='SHA1 Password Cracker using a dictionary attack')
    parser.add_argument('hash', help='The hash to crack')
    parser.add_argument('-w', '--wordlist', default='./rockyou.txt', help="The path to the wordlist used for the cracking (default is rockyou.txt)")
    
    args = parser.parse_args()


    crack(args.hash, args.wordlist)
            
        


    



if __name__ == '__main__':
    main()