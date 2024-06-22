with open("text.txt", "r") as f:
    # contents = f.read()
    for line in f:
        print(line, end="")


with open("text.txt", "r") as rf:
    with open("text.txt_copy", "w") as wf:
        for line in rf:
            wf.write(line)


# opening files in binary mode (reading bytes)
with open("dog.img", "rb") as rf:
    with open("dog_img_copy.img", "wb") as wf:
        for line in rf:
            wf.write(line)

# opening files in binary mode (reading bytes) - reading by chunks
with open("dog.img", "rb") as rf:
    with open("dog_img_copy.img", "wb") as wf:
        chunk_size = 4096
        contents_in_bytes = rf.read(chunk_size)
        while len(chunk_size) > 0:
            wf.write(contents_in_bytes)
            contents_in_bytes = rf.read(chunk_size)
