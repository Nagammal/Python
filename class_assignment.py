class SubfieldsInAI():
    def Subfields():
        answerlist=['Sub-fields in AI are:','Machine Learning','Neural Networks','Vision','Robotics','Speech Processing','Natural Language Processing']
        #answer=print("Sub-fields in AI are: \nMachine Learning\nNeural Networks\nVision\nRobotics\nSpeech Processing\nNatural Language Processing")
        for item in answerlist:
            print (item)
        #return answerlist#Create a function to check whether the given number is odd or even
class OddEven():    
    def OddEven():
        num=int(input("Enter a number :"))
        print("Enter a number:",num)
        if(num%2==1):
            answer=print(num,"is Odd Number")
        else:
            answer=print(num,"is Even Number")
        return answer
# Create a function that tells elegibility of marriage for male and female according to their age limit like 21 for male and 18 for female
class ElegiblityForMarriage():
    def Eligible():
        Gender=input("Enter your Gender")
        Age=int(input("Enter your age"))
        print("Your Gender:",Gender)
        print("Your Age:",Age)
        if (Gender=="Male" and Age>=21):
            message=print("ELIGIBLE")
        elif(Gender=="Female" and Age>=18):
            message=print("ELIGIBLE")
        else:
            message=print("NOT ELIGIBLE")
        return message
class FindPercent():
    def percentage():
        Subject1=int(input())
        Subject2=int(input())
        Subject3=int(input())
        Subject4=int(input())
        Subject5=int(input())
        print("Subject1=",Subject1)
        print("Subject2=",Subject2)
        print("Subject3=",Subject3)
        print("Subject4=",Subject4)
        print("Subject5=",Subject5)
        Total=Subject1+Subject2+Subject3+Subject4+Subject5
        percentage=(Total/500)*100
        print("Total=",Total)
        print("percentage=",percentage)