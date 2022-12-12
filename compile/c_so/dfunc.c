#include<stdio.h>
int dgfunc(int n)
{
    if(n < 2){
        return 1;
    }else{
        return dgfunc(n-1)+dgfunc(n-2);
    }
}
