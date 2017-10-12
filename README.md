# sha1crack
mtc3- kitrub- 07

https://www.mysterytwisterc3.org/en/challenges/level-ii/cracking-sha1-hashed-passwords
本题通过键盘指印和已知的hash值来破解密码
键盘上有八个指印，则密码至少有八位。而且有shift键，并且左右都有，说明左半部分和右半部分键盘都有大写的成分，这帮助我们筛选了一些没有必要进行hash检测的值，提高了效率
