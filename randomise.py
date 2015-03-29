#!/usr/bin/env python

from numpy.random import choice as numpy_choice
from random import choice

# class RandomisedPopulation(object):
#     """ Class to deal with stratified block randomisation """
#     def __init__(self, variables, population):
#         super(RandomisedPopulation, self).__init__()
#         self.variables = variables
#         self.population = population


class Participant(object):
    """Class for new Participant, member of population"""
    def __init__(self, participant_id):
        super(Participant, self).__init__()
        self.participant_id = participant_id


def generate_population():
    """Generate a set of participants to define a population.
    Need to generate these automatically"""

    population = []

    return population


def define_stratified_groups():

    """
    Create groups so population is stratified by randomisation variables 
    """

    groups = {}

    # Tuples are hashable in python
    # http://stackoverflow.com/questions/2388302/best-way-to-define-multidimensional-dictionaries-in-python
    variable_set_1 = ['option1', 'option2']
    variable_set_2 = ['optionA', 'optionB']
    variables = [variable_set_1, variable_set_2]

    # Possible to loop through any number of variables?
    # Initialise groups
    for var_1 in variable_set_1:
        for var_2 in variable_set_2:
            groups[(var_1, var_2)] = []

    return groups


def population_to_groups(population, groups):
    """Assign each participant in a population to a stratified group.
    Currently doing this by hardcoding. Need to feed in the
    stratification variables for dynamic allocation."""

    for participant in population:
        if participant.var_1 == 'A':
            if participant.var_2 == 'X':
                groups[('A', 'X')].append(
                    participant.participant_id)
            else:
                groups[('A', 'Y')].append(
                    participant.participant_id)
        else:
            if participant.var_2 == 'X':
                groups[('B', 'X')].append(
                    participant.participant_id)
            else:
                groups[('B', 'Y')].append(
                    participant.participant_id)

    return groups


def define_block():

    # Todo: possible option -> hardcode block size?
    block_size = 8

    # Todo: possible option -> define other arms?
    arms = ['intervention', 'control']
    arm_assignment = {'intervention': 0, 'control': 0}
    arm_list = []

    # Todo: possible option -> include seed for reproducing results
    # seed(74832.9191663033)
    # Need to pass the state of the random generator back to main
    # so that it isn't reset for each loop, which would be pointless

    for x in xrange(0, block_size):

        if (arm_assignment['intervention'] == block_size / 2):
            arm_assignment['control'] += 1
            arm_list.append('control')

        elif (arm_assignment[arms[1]] == block_size / 2):
            arm_assignment[arms[0]] += 1
            arm_list.append('intervention')

        else:
            arm_choice = choice(arms)
            arm_assignment[arm_choice] += 1
            arm_list.append(arm_choice)

    return arm_list


def population_to_blocks(population):

    block_size = 8

    for features, participants in population.items():
        print "\nFeatures: ", features
        print "Participants:", participants

        # Slice notation
        # http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
        blocks = [
                participants[x:x+block_size]
                for x in xrange(0, len(participants), block_size)
                ]
        print "\nBlocks:"
        for block in blocks:

            # Generate new block assignments
            block_assignment = define_block()

            for i, participant in enumerate(block):
                print participant, " - ", block_assignment[i]

    print "\n"


def main():

    # Generate population
    population = generate_population()

    # Define stratified groups
    groups = define_stratified_groups()

    # Population to groups
    population_in_groups = population_to_groups(population, groups)

    # Population to blocks
    population_to_blocks(population_in_groups)

    # Define blocks
    block = define_block()
    print "\nFinished\n"

if __name__ == '__main__':
    main()
