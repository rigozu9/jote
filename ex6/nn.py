import math
import os
import numpy as np
from PIL import Image
import random

NUMBER_OF_PIXELS = 28 * 28
IMAGE_SIZE = 28


def get_chars(filename):
    """
    Reads the classes of characters
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            chars = [line[0] for line in file]

        return chars

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise


def get_images(filename):
    """
    Reads the images (black pixel is 1, white pixel is 0 in the input)
    Trasnforms (0, 1) values to (-1.0, 1.0)
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    vectors = []

    try:
        with open(os.path.join(dir_path, '..', filename)) as file:
            for line in file:
                vectors.append([1.0 if float(v) == 1 else -1.0 for v in line.strip().split(',')])

        return vectors

    except FileNotFoundError:
        print("File %s was not found." % filename)
        raise
    except Exception as e:
        print("Something terrible happened: %s", str(e))
        raise
    
import numpy as np

class NearestNeighbor:
    def __init__(self, images, chars):
        idata = get_images(images)
        cdata = get_chars(chars)
        # Prepare training data
        self.training_data = [
            {'vector': v, 'char': c} for v, c in zip(idata, cdata)]

    def classify(self, test_vector):
        """
        Classifies a test vector by finding the nearest neighbor in the training data.

        :param test_vector: A vector representing the input image
        :return: The class of the nearest neighbor
        """
        closest_distance = float('inf')
        closest_class = None

        for example in self.training_data[:5000]:
            distance = np.linalg.norm(np.array(test_vector) - np.array(example['vector']))  # Euclidean distance

            if distance < closest_distance:
                closest_distance = distance
                closest_class = example['char']

        return closest_class

    def test(self, test_data, test_labels):
        """
        Tests the classifier on a test dataset.

        :param test_data: List of test vectors
        :param test_labels: List of true classes for the test data
        :return: Accuracy (correctly classified / total test examples)
        """
        correct = 0

        for vector, label in zip(test_data, test_labels):
            predicted = self.classify(vector)
            if predicted == label:
                correct += 1

        return correct / len(test_data)
