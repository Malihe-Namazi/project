
import math
counter=1
user_count=int(input('How maney times do want to use the calculater?'))


while (counter<=user_count):
    operator=input('how do you want to be your operator (basic OR advanced)?')
    print('your try:',counter)
    counter+=1
    
    if (operator=='basic'):
        number1=float(input('please enter first number:'))
        basic_op=input('please choose your operator (+,-,*,/,%,//,**):')
        number2=float(input('please enter secant number:'))
         
        print('_________________________________________')
        if(basic_op=='+'):
            sum=number1+number2
            print('sum of numbers:',sum) 
            
        elif(basic_op=='-'):
            sub=number1-number2
            print('subtract of numbers:',sub)  
            
        elif(basic_op=='*'):
            multi=number1*number2
            print('multipliction of numberts:',multi)
            
        elif(basic_op=='/'):
            if(number2==0):
                print('can not divide by zero.')
            else:
                divi=number1/number2
                print('division of numbers:',divi)
                
        elif(basic_op=='%'):
            mod=number1%number2
            print('mod of numbers:',mod)
            
        elif(basic_op=='//'):
            if(number2==0):
                print('can not divide by zero.')
            else:
                quotient=number1//number2
                print('quotient of numbers:',quotient)
                
        elif(basic_op=='**'):
            power=number1**number2
            print('power of number:',power)
        
        else:
            print('please try again.')
            counter-=1
            
    elif(operator=='advanced'):
        advanced_op=input('please choose your operator(\n log2 \t \tlog10 \t \tradical \nsin \t \tcos \t \ttan \nceil \t \tfloor \t \tfabs \nfact \t \tdegree \t \tbmm \nkmm \t \tmax \t \tmin \nprime \t \teven or odd \t \t e \t pi \n: ')
        
        if(advanced_op=='prime' or advanced_op=='even or odd'):
           number=int(input('please enter your number:'))
        
        elif(advanced_op=='pi' or advanced_op=='e'):
            print(' number is:') 
                        
        elif(advanced_op=='bmm' or advanced_op=='kmm'):
            num1=int(input('please enter an intiger number:'))
            num2=int(input('please enter secand intiger number:'))
        else:
            number1=float(input('please enter the number:'))
        if(advanced_op=='max' or advanced_op== 'min'):
            number2=float(input('please enter secant number:'))
         
        print('_________________________________________')
        
        if (advanced_op=='log2'):
            log2=math.log2(number1)
            print('log2 of number:',log2)
            
        elif(advanced_op=='log10'):
            log10=math.log10(number1)
            print('log10 of number:',log10)
    
            
        elif(advanced_op=='radical'):
            radical=math.sqrt(number1)
            print('radical of number:',radical)
            
        elif(advanced_op=='sin'):
            sin=math.sin(number1)
            print('sin of number:',sin)
            
        elif(advanced_op=='cos'):
            cos=math.cos(number1)
            print('cos of number:',cos) 
            
        elif(advanced_op=='tan'):
            tan=math.tan(number1)
            print('ton of number:', tan)
            
        elif(advanced_op=='ceil'):
            ceil=math.ceil(number1)
            print('ceil of number:',ceil)
            
        elif(advanced_op=='floor'):
            floor=math.floor(number1)
            print('floor of number:',floor)
            
        elif(advanced_op=='fabs'):
            fabs=math.fabs(number1)
            print('absolute value of number:',fabs)
            
        elif(advanced_op=='fact'):
            fact=math.factorial(number1)
            print('factorial of number:',fact)
            
        elif(advanced_op=='degree'):
            degree=math.degrees(number1)
            print('degree of numbers:',degree)
            
        elif(advanced_op=='max'):
            max=max(number1,number2)
            print('max of numbers:',max)
            
        elif(advanced_op=='min'):
            min=min(number1,number2)
            print('min of numbers:',min)
            
        elif(advanced_op=='kmm'):
            kmm=math.lcm(num1,num2)
            print('kmm of numbers:',kmm)
            
        elif(advanced_op=='bmm'):
            bmm=math.gcd(num1,num2)
            print('bmm of numbers:',bmm)
    
        elif(advanced_op=='prime'):

            accumulator = 0

            for i in range(1, number+1):
                if number%i == 0:
                    accumulator+=1

            if accumulator==2:
                    print('your number is prime')
            else:
                    print('your number is not prime')
                    
        elif(advanced_op=='even or odd'):
            if(number%2==0):
                print('your number is even.')
            else:
                print('your number id odd.') 
                
        elif(advanced_op=='e'):
              print(math.e)       
                          
        elif(advanced_op=='pi'):
            print(math.pi)
                              
                          
        else:
            print('please try again')
            counter-=1
            
    else:
        print('please try again.')
        counter-=1
    
