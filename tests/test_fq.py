import data
from ltbio.fastq import fastq_get_next_record

fastq_filename = "/home/luisa/test.fq"

first_rec = {
    "name": "HWI12345:a:seq",
    "comment": "1:N:0:0",
    "seq": "ACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGTACGT",
    "qual": "IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIII"
}

def test_fastq_get_next_record():
    fh = open(data.fastq_filename)
    rec = fastq_get_next_record(fh)
    assert(rec == first_rec)
    rec = fastq_get_next_record(fh)
    assert(rec == None)
    fh.close()
