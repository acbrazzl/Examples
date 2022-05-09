#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Node {
    char letter;
    struct Node* next;
    struct Node* last;
};

void printList(struct Node* n){
    printf("Printing List!\n");
    while(n!= NULL){
        printf("%c",n->letter);
        n=n->next;
    }
    printf("\n");
}

void makeList(char *c, struct Node* head){
    printf("Received: %s\n", c);
    int i = 0;
    while (c[i] != '\0'){
        printf("Loading %c into node %d\n", c[i], i);
        //if empty, 
        if(head->letter==NULL){
            head->letter = c[i];
        //else second entry
        }else if(head->next==NULL){
            struct Node* node = malloc(sizeof(struct Node)); 
            node->letter = c[i];
            node->next = NULL;
            node->last = NULL;
            head->next = node;
            head->last = node;
           //printf("Sanity Checking: head->letter=%c\n", head->letter);
        //else nth entry
        }else {
            //printf("Sanity Checking: head->letter=%c\n", head->letter);
            struct Node* node = malloc(sizeof(struct Node)); 
            node->letter = c[i];
            node->next = NULL;
            node->last = NULL;
            head->last->next = node;
            head->last = node;
        }
        i++;
    }

}

int main(){
    
    struct Node* head = NULL; 
    struct Node* second = NULL;
    struct Node* third = NULL;
    struct Node* fourth = NULL;
    struct Node* fifth = NULL;

    head = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    fourth = (struct Node*)malloc(sizeof(struct Node));
    fifth = (struct Node*)malloc(sizeof(struct Node));

    head->letter = 'D';
    head->next = second;

    second->letter = 'o';
    second->next = third;

    third->letter = 'o';
    third->next = fourth;

    fourth->letter = 't';
    fourth->next = fifth;

    fifth->letter = '!';
    //NULL

    printList(head);

    char str[15]= "Hello, World!";
    //char str[15]= "Wuddup";
    //char *p = str;
    struct Node* second_head = (struct Node*)malloc(sizeof(struct Node)); 
    second_head->letter=NULL;
    second_head->next=NULL;
    second_head->last=NULL;
    makeList(str, second_head);
    printList(second_head);

    return 0;
}