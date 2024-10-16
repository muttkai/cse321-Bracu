# -*- coding: utf-8 -*-
"""task2-ch-gch.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vnkaEtxWsw7oJmg02BVkl4ydrfqIW67_
"""

#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>

int main() {
    pid_t pid = fork();

    if (pid == 0) {
        pid_t grandchild_pid = fork();
        if (grandchild_pid == 0) {
            printf("I am grandchild\n");
        } else {
            wait(NULL);
            printf("I am child\n");
        }
    } else {
        wait(NULL);
        printf("I am parent\n");
    }

    return 0;
}