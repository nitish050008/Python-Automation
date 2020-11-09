#https://lm.facebook.com/l.php?u=https%3A%2F%2Fyoutu.be%2Fx084tfX4JnI%3Ffbclid%3DIwAR0j_OQsqIbYKlpOvgrICm2JOBPtt2stylYhimuFzOgiqYDUhsAEndNl4ho&h=AT2b-T68wP1EqLbQG_RSvj3rUuTUx5Fq0eecmX0MWN0gVjAFh1nXqFBmZ67toFaoT7AEVHxKRF-1SgENOg3TmXc9QLyhjsBNbzASrj7Jd5Ge1LeLsbAwFGBfJUavzOL3gxMBRBL4z2je2ZZWV1m9Zg
# subscribed by code house  
# Function for nth Fibonacci number
 

def Fibonacci(n):

    if n<=0:

        print("Incorrect input")

    # First Fibonacci number is 0

    elif n==1:

        return 0

    # Second Fibonacci number is 1

    elif n==2:

        return 1

    else:

        return Fibonacci(n-1)+Fibonacci(n-2)
 
# Driver Program
 

print(Fibonacci(9))
