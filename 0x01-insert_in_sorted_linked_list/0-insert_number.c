#include "lists.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * insert_node - inserts a number into a sorted singly linked list
 *
 * @head: pointer to pointer of first node of listint_t list
 * @number: integer to be included in new node
 *
 * Return: the inserted node or NULL if fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *tmp = NULL, *current = NULL, *new = NULL;

	new = create_node(number);
	if (new == NULL)
		return (NULL);
	if (head == NULL || *head == NULL)
	{
		*head = new;
		return (new);
	}

	tmp = *head;
	current = tmp;

	if (tmp->next == NULL)
	{
		if (tmp->n > number)
		{
			new->next = tmp;
			*head = new;
			return (new);
		}
		tmp->next = new;
		return (new);
	}

	while (tmp)
	{
		if (tmp->n > number)
		{
			new->next = tmp;
			current->next = new;
			return (new);
		}
		current = tmp;
		tmp = tmp->next;
	}

	current->next = new;
	return (new);
}

/**
 * create_node - allocate space for the new node
 *
 * @number: integer to be included in new node
 *
 * Return: the inserted node or NULL if fails
*/
listint_t *create_node(int number)
{
	listint_t *new = NULL;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	return (new);
}
