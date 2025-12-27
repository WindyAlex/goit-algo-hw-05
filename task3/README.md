# Conclusions

## Article 1
For both existing and fake substrings, **Boyer–Moore** demonstrated the fastest execution time.  
KMP was slower but stable, while Rabin–Karp showed the lowest performance.

## Article 2
The results are consistent with Article 1: **Boyer–Moore** was the fastest algorithm for both types of substrings.  
KMP and Rabin–Karp were slower, especially when searching for a non-existing substring.

## Overall
Based on all measurements for both texts and both types of substrings, **Boyer–Moore** is the fastest algorithm overall.  
Therefore, Boyer–Moore proved to be the most efficient substring search algorithm in the tested scenarios.

### Article 1:
Existing substring:  
Boyer-Moore: 0.000115  
KMP: 0.000988  
Rabin-Karp: 0.001768  

Fake substring:  
Boyer-Moore: 0.00018  
KMP: 0.001914  
Rabin-Karp: 0.003505  

### Article 2:
Existing substring:  
Boyer-Moore: 0.000147  
KMP: 0.001439  
Rabin-Karp: 0.002537  

Fake substring:  
Boyer-Moore: 0.000236  
KMP: 0.002594  
Rabin-Karp: 0.004928  