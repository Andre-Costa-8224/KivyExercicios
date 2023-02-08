#include<stdio.h>
#include<unistd.h>
#include<pthread.h>

void *thread_function(void *arg);
int i,j;
int main()
{
    pthread_t a_thread;  //thread declaration  
    pthread_create(&a_thread, NULL, thread_function, NULL);  //thread is created
    //pthread_join(a_thread, NULL);  //process waits for thread to finish

        //Comment this line to see the difference

    printf("Inside Main Program we print even numbers\n");

    for(j=0;j<50;j++)   // Update the number of repetitions not necessarily the same
    {                   // as for the number of repetitions of the thread_function

        if(j%2 == 0)
        {
            printf("%d\n",j);
        }
        sleep(2);
    }
}

void *thread_function(void *arg) 
{
    // the work to be done by the thread is defined in this function

    printf("Inside Thread we prit odd numbers\n");

    for(i=0;i<50;i++)    // Update the number of repetitions not necessarily the same
    {                    // as for the number of repetitions of the thread_function
        if(i%2 > 0)
        {
            printf("%d\n",i);
        }
        sleep(1);
    }
}
