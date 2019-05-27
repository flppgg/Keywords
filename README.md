# Keywords
## Algorithms for extracting keywords from titles of Scientific Articles


By combining the Natural Language Toolkit ([NLTK](https://www.nltk.org/) package, the [Levenshtein](https://pypi.org/project/python-Levenshtein/) algorithm and an ad-hoc algorithm, this script can:
*1.* select possible candidates for keywords within article titles;
*2.* select the most frequent keywords and use them to create a thematic network of scientific publications;

This was written to scale well up to tens of millions of article titles, and millions of keywords. A few optimizations to the algorithm will be added in the following weeks.

This is just a beta project, you can find a visualization of a graph constructed using this algorithm [here](18.191.13.81). 
Thanks to Anvaka for the excellent visualization engine!
