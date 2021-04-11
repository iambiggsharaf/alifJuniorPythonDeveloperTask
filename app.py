class AlifTask:

    def __init__(self, fileName, operationType):
        self.fileName = fileName
        self.operationType = operationType

        f = open(self.fileName)
        r_negative = open("negative_results.txt", "w")
        r_positive = open("positive_results.txt", "w")
        negative = ""
        positive = ""
        for x in f:
            try:
                result = eval(x.replace(" ", self.operationType))
            except ZeroDivisionError:
                continue

            if result > 0:
                positive += str(result) + "\n"
            elif result < 0:
                negative += str(result) + "\n"

        r_negative.write(negative)
        r_positive.write(positive)
        f.close()
        r_negative.close()
        r_positive.close()


makeOperation = AlifTask(input("File Name: "), input("Operation Type: "))