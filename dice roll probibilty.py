import random
def roll_dice(n):
    frequency = [0, 0, 0, 0, 0, 0]
    
    for i in range(n):
        result = random.randint(1, 6)
        frequency[result - 1] += 1
    
    return frequency

def calculate_probability(frequency, n):
    prob = []
    for f in frequency:
        prob.append(f / n)
    return prob

print("Dice Roll Probability Simulator")
num_rolls = int(input("Enter number of times to roll the dice: "))

freq = roll_dice(num_rolls)
prob = calculate_probability(freq, num_rolls)

print("\nFace\tFrequency\tProbability")
for i in range(6):
    print(f"{i+1}\t{freq[i]}\t\t{prob[i]:.3f}")
