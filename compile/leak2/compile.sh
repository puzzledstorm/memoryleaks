gcc -o leak leak.c
valgrind --leak-check=full ./leak