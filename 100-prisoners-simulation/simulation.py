import random

class PrisonerSimulation:
    """A class to simulate the 100 prisoners problem.

    The 100 prisoners problem is a probability puzzle where 100 prisoners must each find their own number in one of 100 boxes. 
    Each prisoner can open up to 50 boxes, and they must follow a specific sequence of box openings. The goal is for all prisoners 
    to find their own number within the allowed number of attempts.

    Attributes:
        prisoner_len (int): The number of prisoners.
        prisoners (list): A list of prisoner numbers.
        early_stop (bool): Flag to indicate if the simulation should stop early if a prisoner fails.

    Methods:
        shuffle_boxes():
        simulate_prisoners_until_pass():
        simulate_prisoners():
        find_number(prisoner):
    """
    def __init__(self, prisoner_len=100, early_stop=False):
        """
        Initializes the simulation with the given parameters.

        Args:
            prisoner_len (int): The number of prisoners. Defaults to PRISONER_LEN.
            boxes (list): The list of boxes. Defaults to BOXES.
            early_stop (bool): Flag to indicate if the simulation should stop early if a prisoner fails. Defaults to False.
        """
        self.prisoner_len = prisoner_len
        self.prisoners = list(range(prisoner_len))
        self.boxes = list(range(prisoner_len))
        self.early_stop = early_stop

    def shuffle_boxes(self):
        """
        Shuffle the boxes randomly.

        This method uses the random.shuffle function to randomly shuffle the order
        of the boxes in the self.boxes list.
        """
        random.shuffle(self.boxes)

    def simulate_prisoners_until_pass(self,limit=1_000_000):
        """
        Simulates the prisoners' problem until a successful outcome is achieved or the attempt limit is reached.

        This method repeatedly calls the `simulate_prisoners` method to simulate the 
        prisoners' problem. It keeps track of the number of failed attempts and prints 
        the fail count, success rate, and success status after each simulation. 

        If the number of failed attempts exceeds `limit`, the simulation stops and prints an abort message.

        Args:
            limit (int, optional): The maximum number of attempts before aborting. Defaults to 1,000,000.

        Returns:
            int: The number of failed attempts before achieving success, or None if the simulation was aborted.
        """
        fail_count = 0
        while True:
            rate, success = self.simulate_prisoners()
            rate_display = "ignored in early stop" if self.early_stop else f"{rate:.2f}"
            print(f"Fail count: {fail_count}, Rate: {rate_display}, Success: {success}")
            if success:
                return fail_count
            fail_count += 1

            if fail_count > limit:
                print(f"Simulation aborted after {limit} failed attempts.")
                return

    def simulate_prisoners(self):
        """
        Simulates the 100 prisoners problem.

        This method shuffles the boxes and then iterates through each prisoner to see if they can find their number.
        If a prisoner finds their number, the success count is incremented. If a prisoner fails to find their number
        and early stopping is enabled, the simulation stops early and returns the success rate and False.
        Otherwise, it returns the success rate and whether all prisoners succeeded.

        Returns:
            tuple: A tuple containing:
            - float: The success rate (number of successful prisoners / total number of prisoners).
            - bool: True if all prisoners succeeded, False otherwise.
        """
        self.shuffle_boxes()
        success_count = 0
        for prisoner in self.prisoners:
            if self.find_number(prisoner):
                success_count += 1
            else:
                if self.early_stop:
                    return success_count / self.prisoner_len, False
        return success_count / self.prisoner_len, success_count == self.prisoner_len

    def find_number(self, prisoner):
        """
        Simulates a prisoner trying to find their own number in the boxes.

        Each prisoner starts by opening the box with their own number. They then follow the sequence of numbers
        in the boxes, opening a new box each time, up to half the total number of prisoners.

        Args:
            prisoner (int): The number representing the prisoner.

        Returns:
            bool: True if the prisoner finds their own number within the allowed number of attempts, False otherwise.
        """
        current_box = prisoner
        for _ in range(self.prisoner_len // 2):
            if self.boxes[current_box] == prisoner:
                return True
            current_box = self.boxes[current_box]
        return False

class RandomChoiceSimulation(PrisonerSimulation):
    """
    A simulation where each prisoner randomly chooses boxes to find their number.

    Methods
    -------
    find_number(prisoner)
        Simulates a prisoner randomly choosing boxes to find their number.

    Attributes
    ----------
    prisoner_len : int
        The total number of prisoners (and boxes).
    boxes : list
        A list representing the boxes, where each index contains a number.
    """
    def simulate_prisoners_until_pass(self):
        """
        Simulates the prisoners' problem until a successful outcome is achieved.

        This method repeatedly calls the `simulate_prisoners` method to simulate the 
        prisoners' problem. It keeps track of the number of failed attempts and prints 
        the fail count, success rate, and success status after each simulation. The 
        simulation continues until a successful outcome is achieved.

        Returns:
            int: The number of failed attempts before achieving success.
        """
        print("Warning: This simulation could run for a very long time.")
        confirmation = input("Do you want to proceed? (yes/no): ").strip().lower()
        if confirmation != 'yes':
            print("Simulation aborted.")
            return None
        return super().simulate_prisoners_until_pass()

    def find_number(self, prisoner):
        """
        Simulates a prisoner randomly choosing boxes to find their number.

        Parameters
        ----------
        prisoner : int
            The number assigned to the prisoner.

        Returns
        -------
        bool
            True if the prisoner finds their number within half the total number of boxes, False otherwise.
        """
        return prisoner in random.sample(self.boxes, k=self.prisoner_len // 2)


def simulate_prisoners():
    simulation = PrisonerSimulation(early_stop=True)
    return simulation.simulate_prisoners_until_pass()

if __name__ == "__main__":
    fail_count = simulate_prisoners()
    print("fail count:", fail_count)