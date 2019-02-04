alphabet = ["a", "b", "c", "�", "d", "e", "f", "g", "�", "h", "�", "i", "j", "k", "l", "m", "n", "o", "�", "p", "r",
                "s", "�", "t", "u", "�", "v", "y", "z"] 
def findIndex(char):
    index = alphabet.index(char)
    return index

print("2x2 Boyutunda bir anahtar matrisi olu�turun.-->")
matrix = [[0, 0], [0, 0]]
i, j = 0, 0
for i in range(2):
    for j in range(2):
        num = int(input("%d.Sat�r %d.S�tunu Girin: " % (i + 1, j + 1)))
        matrix[i][j] = num

#ENCRYPT KODLARI-------------------------------------------------------->
password = input("�ifrelenecek metni girin: ").lower().replace(" ","")

result,result2,control,count,extra = 0,0,0,0,""
encryptedText = ""

for ccount in password:
    count+=1

if(count%2 != 0):
    extra = input("�kili denkle�tirme i�in ekstra karakteri se�in: ")

for i in password:
    if(control==0):
        result = findIndex(i) * matrix[0][0]
        result2 = findIndex(i) * matrix[1][0]
        control+=1
    elif(control==1):
        result += findIndex(i) * matrix[0][1]
        result2 +=  findIndex(i) * matrix[1][1]
        control=0
        charIndex = result % 29
        charIndex2 = result2 % 29
        encryptedText += alphabet[charIndex]
        encryptedText += alphabet[charIndex2]
        result,result2 = 0,0
if(extra!=""):
    result = findIndex(password[count-1]) * matrix[0][0]
    result2 = findIndex(password[count-1]) * matrix[1][0]
    result += findIndex(extra) * matrix[0][1]
    result2 += findIndex(extra) * matrix[1][1]
    charIndex = result % 29
    charIndex2 = result2 % 29
    encryptedText+= alphabet[charIndex]
    encryptedText+=alphabet[charIndex2]
print("------------------------------------------------------------")
print("��FRELENECEK MET�N ==>",password+extra,"<==")
print("��FRELENM�� HAL�==>",encryptedText,"<==")

#DECRYPT KODLARI-------------------------------------------------------->
determinant = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
inverseMatrix = [[matrix[1][1]*1/determinant,-matrix[0][1]*1/determinant],[-matrix[1][0]*1/determinant,matrix[0][0]*1/determinant]]
password = ""
control,resultE,resultE2 = 0,0,0
for i in encryptedText:
    if(control==0):
        resultE = findIndex(i) * inverseMatrix[0][0]
        resultE2 = findIndex(i) * inverseMatrix[1][0]
        control+=1
    elif(control==1):
        resultE += findIndex(i) * inverseMatrix[0][1]
        resultE2 += findIndex(i) * inverseMatrix[1][1]
        password += alphabet[int(resultE % 29)]
        password += alphabet[int(resultE2 % 29)]
        resultE,resultE2 = 0,0
        control = 0
print("��FREN�N ��Z�LM�� HAL�==>",password,"<==")
print("------------------------------------------------------------")
