#include <stdlib.h>

void leak(int n)
{
    size_t blocksize = 1024 * 1024;
    void* block = malloc(blocksize*n);
    return;
}
 

int main (void){
    leak(2); 
    return 0;
}