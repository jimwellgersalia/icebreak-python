class Divisible():
    def by_seven(self, n):
        for num in range(0, n+1):
            if num % 7 == 0:
                yield num


divisible = Divisible()
generator = divisible.by_seven(int(input('Please enter a number: ')))

for number in generator:
    print(number)
