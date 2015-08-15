#RarPassword Cracker in python.

I had to bruteforce a rar file in a ctf so wrote some ad-hoc code in python. 
Works in Linux.

```python
python bruteforce.py -f filetocrack.rar -c charset -n sizeofpassword

python bruteforce.py -f example.rar -c abcdefghijklmnopqrst0123 -n 6
```

