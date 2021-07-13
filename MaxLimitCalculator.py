from Calculator import Calculator

class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100:
            print("values cant be over 100 add a number under %d" % (100-(self.value-val)))
            self.value -= val

cal = MaxLimitCalculator()
cal.add(50)
cal.add(40)
cal.add(60)
print(cal.value)