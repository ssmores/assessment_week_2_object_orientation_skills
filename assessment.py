"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

   The three main design advantages object orientation provides is
   encapsulation, abstraction, and polymorphism. 

   Encapsulation is when data and its functions are all packaged
   closely together (in a class).  Small bits of code are used
   to make something larger. 

   Abstraction is when a user of a class doesn't need to know how 
   the features or methods in the class work, but they know that 
   it just works.  (They don't need to the inner guts of how 
    something works, only that it is working.)

    Polymorphism is when a class is written in a "general" way, so that
    its subclasses can use the superclass' existing structure.  (The 
    superclass is written in such a way that it's flexible to handle
    generic/unknonw cases, whereas the subclasses are defined specific
    types of those things.)

2. What is a class?
    A class is a structure to describe general attributes of a thing.
    You can define a class to define attributes for an instance of
    that class thing, and also create methods to act upon that instance.
    Once you define a class, you can use it to create instances of 
    said class in your code.  
    (Lists, strings, dictionaries, etc., are classes.)

3. What is an instance attribute?
    An instance attribute is when that attribute is given/defined
    for that specific instance.  For example, an animal name is 
    an instance attribute (your cat may be named fluffy, mine may
    be called Fluffst4r).

4. What is a method?
    A method is a function that has been defined to be used on 
    a specific class.

5. What is an instance in object orientation?
    When you create a new thing using a class, you are instantiating
    a new instace of that class. It is an individual creation 
    of a particular class (if I created a new list, called my_list, 
        and bound it to an empty list, my_list is an instance of 
        the List class). 

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

   A class attribute is one that set by the class (sort of like a
    default attribute value), versus an instance attribute that is 
    set for the individual instance.  If an attribute hasn't been
    set for an individual instance, the attribute would be set by 
    the class. For example, the number_of_legs attribute is set in 
    my Animal class as 4.  When a new instance is created using the 
    Animal class, and the number_of_legs attribute for that instance
    is set to a value, say 2, then the instance attribute for this 
    specific instance is 2.  However, if I create another instance
    using the Animal class, and I don't set the instance attribute 
    for number_of_legs, it doesn't have an instance attribute, but 
    it does has the class attribute set as 4. 


"""


# Parts 2 through 5:
# Create your classes and class methods

# Part 2
class Student(object): 
    """Student class, which needs the first name, last name, and address."""

    def __init__(self, first_name, last_name, address):
        """Provide the first name, last name, and address for this dunder init method."""
        
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

    def info(self):
        """Returns a dictionary of info on this student"""
        
        student_info = {'first name' : self.first_name, 
                        'second name' : self.last_name, 
                        'address' : self.address,
                        }
        return student_info



class Question(object):
    """Question class, which needs question and correct answer."""

    def __init__(self, question, correct_answer):
        """Provide an exam question and the correct answer."""
        
        self.question = question
        self.correct_answer = correct_answer

    def question_info(self):
        """The question and correct answer is stored in the test_info dictionary."""

        test_info = {'question' : self.question, 
                    'correct_answer' : self.correct_answer,
                    }

        return test_info



class Exam(object):
    """Exam class needs the exam name and a list of questions."""

    def __init__(self, name, questions):
        """Requires name, and questions information."""
        self.name = name
        self.questions = questions
        
