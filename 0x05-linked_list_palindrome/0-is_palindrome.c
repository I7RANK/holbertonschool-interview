#include "lists.h"

listint_t *check_palindrome(listint_t *head, listint_t *tmp);

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a pointer to the first node in the linked list
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 * An empty list is considered a palindrome
*/
int is_palindrome(listint_t **head)
{
	listint_t *node = NULL;

	if (*head == NULL)
		return (1);

	node = check_palindrome(*head, *head);

	if (node != NULL)
		return (1);
	return (0);
}

/**
 * check_palindrome - made a recursion to compare the nodes
 * @head: a pointer to the first node in the linked list
 * @tmp: a pointer to the first node in the linked list
 *
 * Return: the node to compare, from start to finish
*/
listint_t *check_palindrome(listint_t *head, listint_t *tmp)
{
	listint_t *node = head;

	if (tmp->next)
	{
		node = check_palindrome(head, tmp->next);
		if (node == NULL)
			return (node);
	}

	if (node->n == tmp->n)
	{
		if (node->next)
			return (node->next);
		else
			return (node);
	}

	return (NULL);
}
