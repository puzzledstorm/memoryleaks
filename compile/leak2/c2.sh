gcc -g leak2.c -o leak
valgrind --leak-check=full ./leak