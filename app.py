class AlifTask:

    def __init__(self, fileName, operationType):
        self.fileName = fileName
        self.operationType = operationType

        f = open(self.fileName)
        r_negative = open("negative_results.txt", "w")
        r_positive = open("positive_results.txt", "w")

        for x in f:
            try:
                result = eval(x.replace(" ", self.operationType))
            except ZeroDivisionError:
                continue

            if result > 0:
                r_positive.write(str(result) + "\n")
            elif result < 0:
                r_negative.write(str(result) + "\n")

        f.close()
        r_negative.close()
        r_positive.close()


makeOperation = AlifTask(input("File Name: "), input("Operation Type: "))