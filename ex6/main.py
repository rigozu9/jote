from perceptron import Perceptron
from nn import NearestNeighbor

IMGS_FILE = 'mnist-x.data'
CHARS_FILE = 'mnist-y.data'

def main():
    #ex5

    """
    Implement the perceptron algorithm in the Perceptron class. After that you can try out the
    values of different number pairs by changing the values of the 'target_char' and
    'opposite_char' variables.
    """
    # perc = Perceptron(IMGS_FILE, CHARS_FILE)
    # perc.train('7', '5', 100)
    # print("7 and 5", perc.test('7', '5'))
    # perc.save_weights('weights.bmp')

    # perc.train('3', '5', 100)
    # print("3 and 5 ",perc.test('3', '5'))
    # perc.save_weights('weights.bmp')

    #ex6
    
    """
    Implement and test the nearest neighbor classifier for MNIST.
    """
    print("Nearest Neighbor Classifier")

    # Initialize Nearest Neighbor classifier
    nn = NearestNeighbor(IMGS_FILE, CHARS_FILE)

    print("3 vs 5")
    test_data = [e for e in nn.training_data[5000:] if e['char'] in ('3', '5')]
    # print("1 vs 0")
    # test_data = [e for e in nn.training_data[5000:] if e['char'] in ('1', '0')]
    # print("1 vs 0")
    # test_data = [e for e in nn.training_data[5000:] if e['char'] in ('1', '0')]

    test_vectors = [e['vector'] for e in test_data]
    test_labels = [e['char'] for e in test_data]

    accuracy = nn.test(test_vectors, test_labels)
    print(accuracy)


if __name__ == '__main__':
    main()
