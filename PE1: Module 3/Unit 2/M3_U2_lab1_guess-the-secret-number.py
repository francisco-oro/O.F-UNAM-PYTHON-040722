secret_number = 777
givenNumber = 0
print(
"""
+==================================+
| Welcome to my game, muggle!      |
| enter an integer                 |
| and guess the number I've        |
| choosen for you.                 |
| Then,                            |
| What is the secret number?       |
+==================================+
""")

while givenNumber != secret_number:
    try:
        givenNumber = int(input("What is the secret number?: "))
        if givenNumber != secret_number: 
            print("Ha, ha! You're stuck in my loop!")
    except:
        print("Ha, ha! You're stuck in my loop!")

print("Nicely done, muggle! You're free now")
