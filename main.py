from Bio import SeqIO
input_file = open("NIHMS926583-supplement-2.fasta", "r")
output_file = open("output.txt", "w")

for seq_record in SeqIO.parse(input_file, "fasta"):
    print(seq_record.id)
    print(seq_record.seq)
    print(len(seq_record))

#hello