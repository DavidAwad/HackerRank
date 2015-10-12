n = int(input())

my_list = [int(s) for s in input().split()]

positives = len(list(filter(lambda x: x > 0, my_list)))

negatives = len(list(filter(lambda x: x < 0, my_list)))

print(positives/n)

print(negatives/n)

print((n - positives - negatives)/n)

