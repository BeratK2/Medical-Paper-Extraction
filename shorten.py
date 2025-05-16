def keep_first_10_jsonl(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as infile, \
         open(output_path, 'w', encoding='utf-8') as outfile:
        for i, line in enumerate(infile):
            if i >= 50:
                break
            outfile.write(line)

# Example usage:
keep_first_10_jsonl('proton2.jsonl', 'proton2_first10.jsonl')
