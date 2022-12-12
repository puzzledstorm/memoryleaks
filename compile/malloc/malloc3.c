#include <stdio.h>
#include <stdlib.h>
 
 
int main(int argc, char** argv)
{
    size_t blocksize = 1024 * 1024;
    int n = 2;
    void* block = malloc(blocksize*n);
    printf("%p\n", block);

    if (block)
    {
        free(block);
    }
 
    printf("malloc size = %dM\n", n);
    return 0;
}