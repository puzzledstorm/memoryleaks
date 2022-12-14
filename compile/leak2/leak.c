#include <stdlib.h>

void func (void){
    char *buff = (char*)malloc(10);
}

int main (void){
    func(); // 产生内存泄漏
    return 0;
}