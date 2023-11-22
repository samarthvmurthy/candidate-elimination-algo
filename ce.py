import csv
import numpy as np

def read_examples_from_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        examples = [row for row in reader]
    return np.array(examples)

def candidate_elimination(examples):
    specific_hypothesis = examples[0][:-1]
    general_hypothesis = [['?' for _ in range(len(specific_hypothesis))]]

    for example in examples:
        if example[-1] == 'Y':
            for i in range(len(specific_hypothesis)):
                if example[i] != specific_hypothesis[i]:
                    specific_hypothesis[i] = '?'

            general_hypothesis_copy = general_hypothesis.copy()
            for hypothesis in general_hypothesis_copy:
                for i in range(len(hypothesis)):
                    if example[i] != hypothesis[i] and hypothesis[i] != '?':
                        general_hypothesis.remove(hypothesis)
                        break

        else:
            if np.array_equal(example[:-1], specific_hypothesis):
                specific_hypothesis = ['?' for _ in range(len(specific_hypothesis))]

            new_general_hypotheses = []
            for hypothesis in general_hypothesis:
                for i in range(len(hypothesis)):
                    if hypothesis[i] == '?':
                        new_hypothesis = hypothesis.copy()
                        new_hypothesis[i] = example[i]
                        new_general_hypotheses.append(new_hypothesis)
            general_hypothesis = new_general_hypotheses

    return specific_hypothesis, general_hypothesis


filename = 'examples.csv'
examples = read_examples_from_csv(filename)

specific, general = candidate_elimination(examples)
print("Specific Hypothesis:", specific)
print("General Hypothesis:", general)
