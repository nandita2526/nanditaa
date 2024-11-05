//implementation of table reservation
#include <stdio.h>
#include <stdlib.h>

#define MAX_TABLES 10  // Maximum number of tables in the restaurant

// Queue structure
struct Queue {
    int tables[MAX_TABLES];  // Array to hold table numbers
    int front;
    int rear;
    int count;
};

// Function prototypes
void initializeQueue(struct Queue *q);
int isFull(struct Queue *q);
int isEmpty(struct Queue *q);
void bookTable(struct Queue *q, int tableNumber);
void cancelTable(struct Queue *q);
void displayFreeTables(struct Queue *q);
void displayTotalTables();

int main() {
    struct Queue reservationQueue;
    initializeQueue(&reservationQueue);
    int choice, tableNumber;

    do {
        printf("\nRestaurant Table Reservation System:\n");
        printf("1. Book a table\n");
        printf("2. Cancel a table\n");
        printf("3. Display number of free tables\n");
        printf("4. Display total number of tables\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                if (!isFull(&reservationQueue)) {
                    printf("Enter table number to book (1 to %d): ", MAX_TABLES);
                    scanf("%d", &tableNumber);
                    if (tableNumber > 0 && tableNumber <= MAX_TABLES) {
                        bookTable(&reservationQueue, tableNumber);
                    } else {
                        printf("Invalid table number.\n");
                    }
                } else {
                    printf("All tables are reserved. No free tables available.\n");
                }
                break;
            case 2:
                cancelTable(&reservationQueue);
                break;
            case 3:
                displayFreeTables(&reservationQueue);
                break;
            case 4:
                displayTotalTables();
                break;
            case 5:
                printf("Exiting the program.\n");
                break;
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 5);

    return 0;
}

// Initialize the queue
void initializeQueue(struct Queue *q) {
    q->front = 0;
    q->rear = -1;
    q->count = 0;
}

// Check if the queue is full
int isFull(struct Queue *q) {
    return q->count == MAX_TABLES;
}

// Check if the queue is empty
int isEmpty(struct Queue *q) {
    return q->count == 0;
}

// Book a table (enqueue operation)
void bookTable(struct Queue *q, int tableNumber) {
    if (isFull(q)) {
        printf("All tables are reserved.\n");
        return;
    }
    q->rear = (q->rear + 1) % MAX_TABLES;
    q->tables[q->rear] = tableNumber;
    q->count++;
    printf("Table %d has been booked.\n", tableNumber);
}

// Cancel a table (dequeue operation)
void cancelTable(struct Queue *q) {
    if (isEmpty(q)) {
        printf("No reservations to cancel.\n");
        return;
    }
    int cancelledTable = q->tables[q->front];
    q->front = (q->front + 1) % MAX_TABLES;
    q->count--;
    printf("Table %d reservation has been cancelled.\n", cancelledTable);
}

// Display the number of free tables
void displayFreeTables(struct Queue *q) {
    int freeTables = MAX_TABLES - q->count;
    printf("Number of free tables: %d\n", freeTables);
}

// Display the total number of tables
void displayTotalTables() {
    printf("Total number of tables: %d\n", MAX_TABLES);
}