# -*- coding: utf-8 -*-
"""task1syscall.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vnkaEtxWsw7oJmg02BVkl4ydrfqIW67_
"""

#include <stdio.h>

struct Item {
    int quantity;
    float unit_price;
};

int main() {
    struct Item paratha, vegetable, water;
    int num_people;
    float total_bill, per_person;

    printf("Quantity Of Paratha: ");
    scanf("%d", &paratha.quantity);
    printf("Unit Price: ");
    scanf("%f", &paratha.unit_price);

    printf("Quantity Of Vegetables: ");
    scanf("%d", &vegetable.quantity);
    printf("Unit Price: ");
    scanf("%f", &vegetable.unit_price);

    printf("Quantity Of Mineral Water: ");
    scanf("%d", &water.quantity);
    printf("Unit Price: ");
    scanf("%f", &water.unit_price);

    printf("Number of People: ");
    scanf("%d", &num_people);

    total_bill = (paratha.quantity * paratha.unit_price) +
                 (vegetable.quantity * vegetable.unit_price) +
                 (water.quantity * water.unit_price);

    per_person = total_bill / num_people;

    printf("Individual people will pay: %.2f tk\n", per_person);

    return 0;
}