#include <iostream>
using namespace std;

class Node {
public:
    char letter;
    Node* next;
    Node(){
        letter = ' ';
        next = NULL;
    }
};

void printList(Node* n){
    while(n != NULL){
        printf("%c", n->letter);
        n = n->next;
    }
}

int main(){
    std::cout << "Doot Doot!\n";

    Node* head = new Node();
    Node* second = new Node();
    Node* third = new Node();
    Node* fourth = new Node();
    Node* fifth = new Node();

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
    printf("\n");
    return 0;
}