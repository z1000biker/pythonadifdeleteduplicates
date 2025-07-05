input_file = "14112021.ADI"
output_file = "logbook_deduped.adi"

seen_records = set()
current_record = []
deduped_lines = []

with open(input_file, "r", encoding="utf-8") as infile:
    for line in infile:
        current_record.append(line)
        if "<EOR>" in line:
            record_text = "".join(current_record)
            if record_text not in seen_records:
                seen_records.add(record_text)
                deduped_lines.extend(current_record)
            current_record = []

# Add any header info (everything before first <a_index>) if needed
with open(input_file, "r", encoding="utf-8") as infile:
    header = []
    for line in infile:
        if "<a_index" in line:
            break
        header.append(line)

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.writelines(header)
    outfile.writelines(deduped_lines)

print("Done! Duplicate records removed.")
