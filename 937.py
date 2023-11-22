def reorderLogFiles(logs):
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

    # logs_list = [logs[i].split(" ") for i in range(len(logs))]
    # digit_log = []
    # for i in range(len(logs_list)):
    #     if(logs_list[i][1].isdigit()):
    #         digit_log.append(logs_list[i])
    # i = 0   
    # while(logs_list[i] in digit_log):
    #     logs[i], logs[i+1] = logs[i+1], logs[i]
    #     i += 1
    
print(reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))