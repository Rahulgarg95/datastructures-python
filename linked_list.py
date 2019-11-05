class Element(object):
    def __init__(self,value):
        self.value=value
        self.next=None
    
    def print_el(self):
        print("Element: ",self.value)

class LinkedList(object):
    #Function for initialization 
    def __init__(self, head=None):
        self.head=head

    #Add new el to end of list
    def append(self, new_el):
        current=self.head
        if(self.head):
            while(current.next):
                current=current.next
            current.next=new_el
        else:
            self.head=new_el

    def get_position(self, pos):
        i=1
        current=self.head
        if(pos<1):
            return None
        while current and i<=pos:
            if(pos==i):
                return current
            current=current.next
            i=i+1
        return None

    def insert(self, new_el, pos):
        i=1
        current=self.head
        if(pos>1):
            while current and i<pos:
                if(i==pos-1):
                    new_el.next=current.next
                    current.next=new_el
                current=current.next
                i=i+1
        elif pos==1:
            new_el.next=self.head
            self.head=new_el

    def delete(self, value):
        current=self.head
        previous=None
        while current.value !=value and current.next:
            previous=current
            current=current.next
        if current.value == value:
            if previous:
                previous.next=current.next
            else:
                self.head=current.next

    def printlist(self):
        current=self.head
        while current:
            print(current.value," --> ")
            current=current.next

a=Element(11)
b=Element(22)
c=Element(33)
d=Element(44)
e=Element(55)

a.print_el()
b.print_el()
c.print_el()
d.print_el()
e.print_el()

l1=LinkedList(a)
l1.append(b)
l1.append(c)

l1.insert(d, 3)
print(l1.get_position(3).value)

l1.insert(e,4)
print(l1.get_position(4).value)

print("Print el ",l1.head.next.next.next.next.value)

val=2
print(l1.get_position(val).value)

l1.printlist()

l1.delete(44)

l1.printlist()