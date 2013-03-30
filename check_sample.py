#!/usr/bin/env python

from pythonipsum import sample, dictionary


def main():
    unused_terms = find_unused_terms(dictionary, sample)
    print "Unused terms:"
    for term in unused_terms:
        print term


def find_unused_terms(dictionary, sample):
    unused_terms = []

    sample = sample.lower()
    for term in dictionary:
        if term.lower() not in sample:
            unused_terms.append(term)

    unused_terms.sort()
    return unused_terms


if __name__ == '__main__':
    main()
