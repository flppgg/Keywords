# Keywords
## Algorithms for extracting keywords from titles of Scientific Articles


By combining the Natural Language Toolkit ([NLTK](https://www.nltk.org/)) package, the [Levenshtein](https://pypi.org/project/python-Levenshtein/) algorithm and an ad-hoc algorithm, this script can:

1. Given a list of Scientific Articles titles, extract potential good keywords from titles;
2. Select the best keywords by looking at their relative frequency, and use them to create a thematic network of scientific publications.

This was written to scale well up to tens of millions of article titles, and millions of keywords. A few optimizations to the algorithm will be added in the following weeks.

This is just a beta project, you can find a visualization of a graph constructed using this algorithm [here](http://18.191.13.81/#/?_k=hvtoo8). 
Thanks to [Anvaka](https://github.com/anvaka) for the excellent visualization engine!
