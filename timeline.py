"""Timeline plot generator for tweet streams."""
from opster import command


@command()
def timeline(
    input_file,
    output=('o', 'timeline.png', 'The output file name.'),
):
    """Generate a timeline plot for a stream of tweets."""
    print('input_file is: {}'.format(input_file))
    print('output is: {}'.format(output))


if __name__ == '__main__':
    timeline.command()
