# SHA1 Password Cracker

A simple Python script to crack SHA1 hashes using a dictionary attack with the `rockyou.txt` wordlist.

If the wordlist is not found, it will be downloaded automatically.

---

## How to Use

**Run the script:**

```bash
python sha1_cracker.py <SHA1_HASH>
````

Example:

```bash
python sha1_cracker.py 5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8
```

**To use a custom wordlist:**

```bash
python sha1_cracker.py <HASH> -w /path/to/wordlist.txt
```

## Notes

* `rockyou.txt` will be downloaded automatically if it's not in the folder.
* Make sure you have Python 3 installed.

## Example Output

```bash
[+] The password is: password
```

## Disclaimer

For educational use only.
