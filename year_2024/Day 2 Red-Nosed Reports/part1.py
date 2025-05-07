def generate_molecules():
    replacements = []
    medicine = ""
    results = set()

    with open("input.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if "=>" in line[:10]:
                source, target = line.split("=>", 1)
                replacements.append((source.strip(), target.strip()))
            else:
                medicine += line

    for source, target in replacements:
        pos = 0
        while pos < len(medicine):
            pos = medicine.find(source, pos)
            if pos == -1:
                break

            new_molecule = medicine[:pos] + target + medicine[pos + len(source):]
            results.add(new_molecule)

            pos += 1

    return len(results)


if __name__ == "__main__":
    distinct_molecules = generate_molecules()
    print(f"Distinct molecules: {distinct_molecules}")
