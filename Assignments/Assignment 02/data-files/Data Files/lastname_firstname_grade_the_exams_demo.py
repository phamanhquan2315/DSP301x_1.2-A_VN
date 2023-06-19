import re
filename = input("Enter a fileName: ")

cntValid =0
cntInValid = 0
lstInValid = []
lstValid = []
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
lst_answer = answer_key.split(',')
lst_point = []
cntHighScore = 0
highestScore =0
lowestScore = 100000
avgScore=  0
sumScore = 0
lst_question_skip = [0 for i in range(26)]
highest_question_skip =0
lst_question_fault = [0 for i in range(26)]
highest_question_fault = 0
lst_class_grade = []

try:
    if filename == "class1":
        with open("class1.txt","r") as f:
            file = f.readlines()
        print("Successfully opened",filename+".txt")
        print('Total lines of data:',len(file))
        for it in file:
            val = it.split(',')
            if len(val) == 26:
                cntValid +=1
                lstValid.append(val)
            else:
                cntInValid+= 1
                lstInValid.append(it)
        for it in lstInValid:
            print('Invalid line of data: does not contain exactly 26 values:')
            print(it)
        print('Total valid lines of data:', cntValid)
        print('Total invalid lines of data:', cntInValid)
        print(lst_answer)
        for it in lstValid:
            point = 0
            for i in range(1, len(it)):
                if (it[i] == lst_answer[i - 1] and it[i] != ''): point += 4
                if (it[i] == ''):
                    lst_question_skip[i] += 1
                    continue
                if (it[i] != lst_answer[i - 1]):
                    point -= 1
                    lst_question_fault[i] += 1
            if point > 80: cntHighScore += 1
            if point > highestScore: highestScore = point
            if point < lowestScore: lowestScore = point
            sumScore += point
            lst_point.append(point)
            lst_class_grade.append([it[0], point])
        print("Total student of high scores:", cntHighScore)
        print("Mean (avg) score:", "{:.3f}".format(sumScore / cntValid))
        print('Highest score:', highestScore)
        print('Lowest score:', lowestScore)
        print('Range of score:', highestScore - lowestScore)
        # tinh trung vi
        lst_point.sort()
        print(lst_point)
        lenght = len(lst_point)
        if (lenght % 2 == 0):
            print("Medium score:", lst_point[lenght // 2])
        else:
            print("Medium score:", (lst_point[lenght // 2] + lst_point[lenght // 2 + 1]) // 2)
        # cau hoi bi bo nhieu nhat
        print("Question that most people skip:",end=" ")
        for it in lst_question_skip:
            if it > highest_question_skip: highest_question_skip = it
        for i in range(len(lst_question_skip)):
            if (lst_question_skip[i] == highest_question_skip): print(i, '-', lst_question_skip[i], '-',"{:.3f}".format(lst_question_skip[i] / cntValid),end=' , ')
        print()
        # cau hoi sai nhieu nhat
        print("Question that most people are fault:",end=" ")
        for it in lst_question_fault:
            if it > highest_question_fault: highest_question_fault = it
        for i in range(len(lst_question_fault)):
            if (lst_question_fault[i] == highest_question_fault): print(i, '-', lst_question_fault[i], '-',"{:.3f}".format(lst_question_fault[i] / cntValid),end=' , ')
        print()
        with open("class1_grades.txt", 'w') as f:
            for it in lst_class_grade:
                f.write(it[0] + "," + str(it[1]) + '\n')

    elif filename == "class2":
        with open("class2.txt","r") as f:
            file = f.readlines()
        print("Successfully opened",filename+".txt")
        print('Total lines of data:', len(file))
        for it in file:
            val = it.split(',')
            if len(val) == 26 and len(val[0]) == 9:
                cntValid += 1
                lstValid.append(val)
            else:
                cntInValid += 1
                lstInValid.append(it)
            # elif len(val[0])!= 9:
            #     cntInValid += 1
            #     lstInValid.append(it)
        for it in lstInValid:
            print('Invalid line of data: does not contain exactly 26 values:')
            print(it)
        print('Total valid lines of data:', cntValid)
        print('Total invalid lines of data:', cntInValid)
        print(lst_answer)
        for it in lstValid:
            point =0
            for i in range(1,len(it)):
                if(it[i] == lst_answer[i-1] and it[i]!=''): point +=4
                if(it[i] == ''):
                    lst_question_skip[i] += 1
                    continue
                if(it[i] != lst_answer[i-1]):
                    point-=1
                    lst_question_fault[i] += 1
            if point > 80 : cntHighScore+=1
            if point > highestScore : highestScore = point
            if point < lowestScore: lowestScore = point
            sumScore += point
            lst_point.append(point)
            lst_class_grade.append([it[0], point])
        print("Total student of high scores:",cntHighScore)
        print("Mean (avg) score:","{:.3f}".format(sumScore/cntValid))
        print('Highest score:',highestScore)
        print('Lowest score:',lowestScore)
        print('Range of score:',highestScore-lowestScore)
        # tinh trung vi
        lst_point.sort()
        print(lst_point)
        lenght = len(lst_point)
        if (lenght % 2==0): print("Medium score:", lst_point[lenght//2])
        else: print("Medium score:",(lst_point[lenght//2]+ lst_point[lenght//2+1])//2)
        # cau hoi bi bo nhieu nhat
        print("Question that most people skip:")
        for it in lst_question_skip:
            if it > highest_question_skip : highest_question_skip = it
        for i in range(len(lst_question_skip)):
            if (lst_question_skip[i] == highest_question_skip): print(i,'-',lst_question_skip[i],'-',"{:.3f}".format(lst_question_skip[i]/cntValid),end=' , ')
        print()
        # cau hoi sai nhieu nhat
        print("Question that most people are fault:")
        for it in lst_question_fault:
            if it > highest_question_fault : highest_question_fault = it
        for i in range(len(lst_question_fault)):
            if (lst_question_fault[i] == highest_question_fault): print(i,'-',lst_question_fault[i],'-',"{:.3f}".format(lst_question_fault[i]/cntValid),end=' , ')
        with open("class2_grades.txt",'w') as f:
            for it in lst_class_grade:
                f.write(it[0]+","+str(it[1])+'\n')




except IOError:
    print("Sorry, I can't find this filename")


