from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    employee_ids = LinkedList()

    # 2) Insert some sample data using insert_at_front or insert_at_end
    employee_ids.insert_at_front(101)
    employee_ids.insert_at_front(202)
    employee_ids.insert_at_front(303)
    employee_ids.insert_at_front(404)

    # 3) Display the list to verify insertion
    print("Original linked list:")
    employee_ids.display()

    # 4) Call recursive_sum and print the result
    total = employee_ids.recursive_sum()
    print(f"Sum of all employee IDs: {total}")

    # 5) Call recursive_search with a target and print result
    target_id = 202
    found = employee_ids.recursive_search(target_id)
    print(f"Is employee ID {target_id} in the list? {found}")

    # 6) Call recursive_reverse, then display the reversed list
    employee_ids.recursive_reverse()
    print("Reversed linked list:")
    employee_ids.display()