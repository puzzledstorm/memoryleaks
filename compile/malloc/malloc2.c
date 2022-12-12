#include <stdio.h>
#include <stdlib.h>
 
 
int main(int argc, char** argv)
{
    size_t maximum = 0;
    size_t blocksize[] = { 1024 * 1024, 1024, 1};
    for (int i = 0; i < 3; i++)
    {
        maximum = 0;
        for (int count = 1; ; ++count)
        {
            void* block = malloc(maximum + blocksize[i] * count);
            if (block)
            {
                maximum = maximum + blocksize[i] * count;
                free(block);
            }
            else
            {
                break;
            }
        }
    }
 
    printf("maxmium malloc size = %f G", maximum / 1000000000.0);
 
    return 0;
}