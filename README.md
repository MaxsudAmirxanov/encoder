#encoder 
###This is my little encoder program written in **python**. It can be used to encrypt any information in the text without changing its visual content.

##Algorithm.
Russian Russian to begin with, the program at the moment can only work with the Russian language, and the bottom line is that there are letters in the Russian language that are visually identical to some letters from the English alphabet, these are letters: a o c x p y e . And these letters, although they look the same, but they have a different code in Unicode or UTF-8 encoding

We take our sentence that we want to encrypt in the text, and we translate this cipher into binary code, then our task is to encrypt this binary code in our main text, and for this we take our letters (a o c x p y e ), and if we need to encrypt 1, then we change the Russian letter to English, and if 0 then do not change
