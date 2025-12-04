def save_output(text, filename="study_output.txt"):
    with open(filename, "w") as f:
        f.write(text)
    print(f"Saved output to {filename}")