#Rar/Zip Password Cracker in python.

I had to bruteforce a rar file in a ctf so wrote some ad-hoc code in python. 
Works in Linux/Windows.


```python```

`python bruteforce.py --fr filetocrack.rar -c charset -n sizeofpassword`

`python bruteforce.py --fr RARFILE.rar -c abcdefghijklmnopqrst0123 -n 6`

`python bruteforce.py --fz ZIPFILE.zip -c charset -n sizeofpassword`

