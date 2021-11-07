# Black-Box-Testing

Description of Project:  
You will write a series of unit tests to test a function called credit_card_validator (written for you) that is passed a sequence of digits as a string that represents a credit card number. This function will return True if it is a valid credit card number, otherwise, it will return False.

Depending on the credit card issuer, the length of a credit card number can range between 10 and 19 digits. The first few digits of the number are the issuer prefix. Each credit card issuer has an assigned range of numbers. For example, only Visa credit card numbers may begin with 4, while American Express card numbers must begin with either a 34 or 37. Sometimes, credit card providers are assigned multiple ranges. For example, MasterCard card numbers must start with the numbers between 51 through 55 or 2221 through 2720 (inclusive). 

The last digit of the number is referred to as the check digit and acts as a checksum. Most credit cards calculate this check digit using the Luhn algorithm (see resources below for how this is calculated).

In order to limit the scope of this assignment, we are going to limit the number of credit card issuers to 3: Visa, MasterCard, and American Express. Each has its own prefixes and length requirements.

Visa:  
* Prefix(es): 4  
* Length: 16  
MasterCard:  
* Prefix(es): 51 through 55 and 2221 through 2720  
* Length: 16    
American Express:  
* Prefix(es): 34 and 37  
* Length: 15  


Cited Work:  
What was used to get credit card numbers implemented: (https://www.dcode.fr/luhn-algorithm) (https://bestccgen.com/)  
Exploration: Category Partition Module and Videos  
Exploration: Black Box Testing (https://replit.com/@coeCS362/blackbox1)  
