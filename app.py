class AlifTask:
    
    def __init__(self, fileName, operationType):
        self.fileName = fileName
        self.operationType = operationType

    def run(self):
        f = open(self.fileName)
        r_negative = open("negative_results.txt", "w")
        r_positive = open("positive_results.txt", "w")
        for x in f:
            a, b = x.split()

            try:
                result = eval(a + self.operationType + b)
            except ZeroDivisionError:
                continue

            if result > 0:
                r_positive.write(str(result) + "\n")
            elif result < 0:
                r_negative.write(str(result) + "\n")


makeOperation = AlifTask(input("File Name: "), input("Operation Type: "))
makeOperation.run()