# need to parse a fastq file
#
# need to read in parameters like window size, quality threshold
#
# need to work out how you are going to trim i.e. when to trim the start of the
# verse the end and how many poor quality bases you need to see before trimming
#
# then need to work out a way of outputting the reads so tha pair information
# is retained and a strategy for singletons.


def do_it_as_a_list():
    l = []
    for n, a in db.query("SELECT name, age FROM table WHERE name = 'Luisa'"):
        n = n.lower()
        a = a - 30 * pi
        l.append((n, a))
    return l


def do_it_as_a_list():
    for n, a in db.query("SELECT name, age FROM table WHERE name = 'Luisa'"):
        n = n.lower()
        a = a - 3
        yield (n, a)


for n, a in db.blah():
    print(n, a)


def window_mean_scores(qualscores, winlen=10, phread=33):
    return []
