#include "lists.h"

/**
 * check_cycle - checks if a lnkd list contains tha cycle
 * @list: linked list to check
 *
 * Return: 1 if tha list is cycle, 0 if not
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	if (!list)
		return (0);

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}

