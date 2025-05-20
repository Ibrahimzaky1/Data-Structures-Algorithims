class singlyNode:  # ❌ You wrote ".class", which is invalid
    def __init__(self, val, next=None):
        self.val = val  # ❌ You forgot to assign self.val
        self.next = next

    def __str__(self):
        return str(self.val)

# Creating nodes
Head = singlyNode(1)
A = singlyNode(3)
B = singlyNode(4)
C = singlyNode(7)

# Linking nodes
Head.next = A
A.next = B
B.next = C

# Print head value
print(Head)

# Traverse and print each node
curr = Head
while curr:
    print(curr)
    curr = curr.next

# Display function
def display(Head):
    curr = Head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' -> '.join(elements))

display(Head)

# ❌ You forgot the colon (:) in the function definition
def search(Head, val):
    curr = Head
    while curr:
        if val == curr.val:
            return True
        curr = curr.next
    return False

# Call and print the result of search
print(search(Head, 2))  # This will print False



class DoublyNodes:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)
    

head = tail = DoublyNodes(1)
print(tail)

def display(head):
    curr = head
    elements = []
    while curr:
        elements.append(str(curr.val))
        curr = curr.next
    print(' <-> '.join(elements))

display(head)

def insert_at_beginnig(head, tail, val):
    new_node = DoublyNodes(val, next=head)
    head.prev = new_node
    return new_node, tail

head, tail = insert_at_beginnig(head, tail, 3)
display(head)

def insert_at_end(head, tail, val):
    new_node = DoublyNodes(val, prev=tail)
    tail.next = new_node
    return head, new_node

head, tail = insert_at_end(head, tail, 7)
display(head)

####################### Lesson 4 #######################

