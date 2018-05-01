# Code-Cleaner
It is often observed that beginners don't indent their code properly.<br/>
For example:<br/>

    int main()
    {
    int a=0,b=0;
    while(++a<5)
    {
    ++b;
    }
    printf("%d %d",a,b);
    }
    
As you can see above, the code hasn't been indented rightly, and as a result it becomes tough to comprehend the code.<br/>
For this reason, this code cleaner script will take your un indented C program and then give out your C program that is indented.


    int main()
    {
      int a=0,b=0;
      while(++a<5)
      {
        ++b;
      }
      printf("%d %d",a,b);
    }
    
After indentation the code is supposed to look like the above version. <br/>

The main code has been written in Python and is in the apps folder. There's also a test code written in C(test.c)<br/>

Run the program by going into the app directory after cloning and then type:

        python3 main.py
        
This will run the program and ask you for typing in the name of the file which you want to indent properly. You can type `test.c`
to check whether the code runs or not!
    
