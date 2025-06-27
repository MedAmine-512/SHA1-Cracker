import hashlib
import argparse
import os
import urllib.request


ROCKYOU_URL = "https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt"

def download():
    print("[*] rockyou.txt not found. Downloading...")
    try:
        urllib.request.urlretrieve(ROCKYOU_URL, './rockyou.txt')
        print("[+] rockyou.txt downloaded successfully.")
    except Exception as e:
        print(f"[!] Failed to download rockyou.txt: {e}")
        exit(1)



def crack(sha1, wordlist):
    if not os.path.isfile(wordlist):
        print(f"[!] Wordlist not found at : {wordlist} ")
        return

    cleaned_sha1 = sha1.strip().lower()


    with open(wordlist, 'r', encoding='latin-1') as passwods:
        
        for line in passwods:
            passwod = line.strip()
            passwod_sha1 = hashlib.sha1( passwod.encode() ).hexdigest()
            if cleaned_sha1 == passwod_sha1:
                print("[+] The password is : ", passwod)
                return
    print('[-] Password not Found')



def main():

    parser = argparse.ArgumentParser(description='SHA1 Password Cracker using a dictionary attack')
    parser.add_argument('hash', help='The hash to crack')
    parser.add_argument('-w', '--wordlist', default='./rockyou.txt', help="The path to the wordlist used for the cracking (default is rockyou.txt)")
    
    args = parser.parse_args()

    if not os.path.isfile('./rockyou.txt'):
        download()

    crack(args.hash, args.wordlist)
            
        


    



if __name__ == '__main__':
    main()