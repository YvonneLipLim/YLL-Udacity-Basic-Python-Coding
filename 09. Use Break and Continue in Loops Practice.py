"""
break and continue are two essential statements in Python used to control the flow of loops.
break terminates the loop entirely, exiting the loop body. An example will be:
for i in range(5):
    if i == 3:
        break
    print(I) #Output: 0, 1, 2

Use Cases for break:
1. Exit the loop when a condition is met.
2. Break out of the loop on error occurrence.

continue skips the current iteration and moves to the next one. An example will be:
for i in range(5):
    if i == 3:
        continue
    print(I) #Output: 0, 1, 2, 4

Use Cases for continue:
1. Skip specific iterations based on conditions.
2. Continue to the next iteration when data doesn't meet the criteria.

Key Points to Note:
1. Loop Types: break and continue work with for and while loops.
2. Nesting: break and continue affect only the innermost loop.
3. Conditional Statements: Use if statements to control break and continue.
4. Loop Variables: Be aware of loop variable values after break or continue.
5. Use return to exit functions.
"""


'''
Q1.
Find two methods to solve the cargo loading program:
Method 1: Breaking out of the loop when the weight limit is reached, however, this method has limitations. 
Method 2: Adding continue by modifying the existing loop condition
'''

#Method 1
all_cargo = [("sofa", 6), ("bananas", 10), ("chair", 20), ("mattresses", 24), ("dog kennels", 42), ("table", 4),("machine", 120), ("cheeses", 5), ("refrigerator", 8)]

print("METHOD 1")
weight = 0 #Sets the initial weight of the container to 0
items = [] #Creates an empty list to store the names of the items loaded into the container
for cargo_name, cargo_weight in all_cargo: #Iterates over each item in the all_cargo list. cargo_name and cargo_weight
    print("current weight: {}".format(weight))
    if weight >= 200: #Checks if the current weight of the container is greater than or equal to 200
        print("  breaking loop now!") #If condition is true, loop is terminated using the break statement, and print message "breaking loop now!"
        break
    else: #If condition is false (i.e., the weight is still below 200), the following actions will continue
        print("  adding {} ({})".format(cargo_name, cargo_weight)) #The current item continue to add to the container
        items.append(cargo_name) #The cargo_name is appended to the items list
        weight += cargo_weight #The cargo_weight is added to the weight of the container

print("\nFinal Weight: {}".format(weight)) #Prints the final weight of the container
print("Final Items: {}".format(items)) #Prints the list of items that were loaded into the container

#Output:
METHOD 1
current weight: 0
  adding sofa (6)
current weight: 6
  adding bananas (10)
current weight: 16
  adding chair (20)
current weight: 36
  adding mattresses (24)
current weight: 60
  adding dog kennels (42)
current weight: 102
  adding table (4)
current weight: 106
  adding machine (120)
current weight: 226
  breaking loop now!

Final Weight: 226
Final Items: ['sofa', 'bananas', 'chair', 'mattresses', 'dog kennels', 'table', 'machine']
---------------------------------------------------------------------------------------------------------------------------------------------------

#Method 2
all_cargo = [("sofa", 6), ("bananas", 10), ("chair", 20), ("mattresses", 24), ("dog kennels", 42), ("table", 4),("machine", 120), ("cheeses", 5), ("refrigerator", 8)]

print("METHOD 2")
weight = 0 #Sets the initial weight of the container to 0
items = [] #Creates an empty list to store the names of the items loaded into the container
for cargo_name, cargo_weight in all_cargo: #Iterates over each item in the all_cargo list. cargo_name and cargo_weight
    print("current weight: {}".format(weight))
    if weight >= 200: #Checks if the current weight of the container is greater than or equal to 200
        print("  breaking from the loop now!") #If condition is true, the loop is terminated using the break statement, and print the message "breaking loop now!"
        break
    elif weight + cargo_weight > 200: #This new condition checks if current weight of the container plus the weight of the current item would exceed weight limit
        print("  skipping {} ({})".format(cargo_name, cargo_weight)) #If condition is true, the continue statement is used to skip the rest of the loop iteration and proceed to the next item 
        continue #Immediately jumps to the next iteration of the loop, skipping the rest of the code within the loop body for the current item
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight)) #Prints a message indicating that the current item is being added to the container, displaying the name and weight of the item added
        items.append(cargo_name) #Adds the name of the current item to the list which keeps track of the items that have been successfully loaded into the container
        weight += cargo_weight #Updates the current weight to reflect the addition of the new item

print("\nFinal Weight: {}".format(weight)) #Prints the final weight of the container
print("Final Items: {}".format(items)) #Prints the list of items that were loaded into the container

#Output:
METHOD 2
current weight: 0
  adding sofa (6)
current weight: 6
  adding bananas (10)
current weight: 16
  adding chair (20)
current weight: 36
  adding mattresses (24)
current weight: 60
  adding dog kennels (42)
current weight: 102
  adding table (4)
current weight: 106
  skipping machine (120)
current weight: 106
  adding cheeses (5)
current weight: 111
  adding refrigerator (8)

Final Weight: 119
Final Items: ['sofa', 'bananas', 'chair', 'mattresses', 'dog kennels', 'table', 'cheeses', 'refrigerator']
---------------------------------------------------------------------------------------------------------------------------------------------------


'''
Q2.
Create a loop with a break statement to create a string, named news_ticker, by concatenating the headlines from a given list, headlines. 
The news_ticker should have a maximum length of 140 characters.

Requirements:
Loop: Use a suitable loop (either for or while) to iterate through the headlines.
Break Statement: Employ a break statement to terminate the loop when the news_ticker reaches 140 characters.
Truncation: If necessary, truncate the last headline to ensure news_ticker is exactly 140 characters long.
Spacing: Insert a space between each headline in the news_ticker.

Example Output:
News Ticker: Headline 1 Headline 2 Headline 3 Headline 4 (truncated)
'''

#Method 1 Using If Statement
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Terrific"]

news_ticker = "" #An empty string that will store the concatenated headline
for headline in headlines: #Variable to keep track of the current length of the news_ticker
    news_ticker += headline + " " #If condition is true, headline is added to the news_ticker with a space after it, and the ticker_length is updated accordingly
    if len(news_ticker) >= 140: #Calculates the length of the news_ticker string then compares the length to 140
        news_ticker = news_ticker[:140] #Creates a new string that consists of the first 140 characters of the original news_ticker and [:140] slicing notation is used to extract the desired substring
        break #Terminates the loop, as the news_ticker has reached its maximum length

print(news_ticker)

#Output:
Local Bear Eaten by Man Legislature Announces New Laws Peasant Discovers Violence Inherent in System Cat Rescues Fireman Stuck in Tree Brave
---------------------------------------------------------------------------------------------------------------------------------------------------

#Method 2 Using If-else Statement
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Terrific"]
news_ticker = "" #An empty string that will store the concatenated headline
ticker_length = 0 #Variable to keep track of the current length of the news_ticker

for headline in headlines: #Iterates through each headline in the headlines list
    if ticker_length + len(headline) <= 140: #Checks if adding current headline to the news_ticker would exceed 140-character limit
        news_ticker += headline + " " #If condition is true, headline is added to the news_ticker with a space after it, and the ticker_length is updated accordingly
        ticker_length += len(headline) + 1
    else: #If condition is false (adding the headline would exceed the limit), the following actions are taken:
        remaining_chars = 140 - ticker_length #Calculates the remaining number of characters allowed in the news_ticker
        news_ticker += headline[:remaining_chars] #Truncates the current headline to fit within the remaining characters and adds it to the news_ticker
        break #Terminates the loop, as the news_ticker has reached its maximum length

print("News Ticker:", news_ticker)

#Output:
News Ticker: Local Bear Eaten by Man Legislature Announces New Laws Peasant Discovers Violence Inherent in System Cat Rescues Fireman Stuck in Tree Brave
---------------------------------------------------------------------------------------------------------------------------------------------------


'''
Q3.
Check if the numbers provided in the list are prime numbers.
If the numbers are prime, the code should print "[number] is a prime number."
If the number is NOT a prime number, it should print "[number] is not a prime number", and a factor of that number, other than 1 and the number itself: "[factor] is a factor of [number]".
Example output:
7 IS a prime number
26 is NOT a prime number, because 2 is a factor of 26
'''

check_prime = [2, 3, 5, 13, 20, 21, 26, 33, 48, 61, 65, 71, 78, 82, 95]
for num in check_prime: #Iterates over each number, num, in the check_prime list
    for i in range(2, num): #Iterates over all integers from 2 up to (but not including) the current number num and checks if any number i within this range divides num evenly.
        if (num % i) == 0: #If num is divisible by i and the remainder of num divided by i is 0, then num is not a prime number
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num)) #Inner loop is immediately terminated using the break statement
            break
        if i == num -1: #If the inner loop completes without finding a divisor of num, it means num is only divisible by 1 and itself, making it a prime number
            print("{} IS a prime number".format(num))

#Output:
3 IS a prime number
5 IS a prime number
13 IS a prime number
20 is NOT a prime number, because 2 is a factor of 20
21 is NOT a prime number, because 3 is a factor of 21
26 is NOT a prime number, because 2 is a factor of 26
33 is NOT a prime number, because 3 is a factor of 33
48 is NOT a prime number, because 2 is a factor of 48
61 IS a prime number
65 is NOT a prime number, because 5 is a factor of 65
71 IS a prime number
78 is NOT a prime number, because 2 is a factor of 78
82 is NOT a prime number, because 2 is a factor of 82
95 is NOT a prime number, because 5 is a factor of 95
