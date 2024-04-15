def truth_table():
    table = []
    for a in range(2):
        for b in range(2):
            for c in range(2):
                result = int(b and a) or int(c and b) or int(a and c)
                table.append((a, b, c, result))
    return table

def canonical_forms(table):
    minterms = []
    maxterms = []
    for entry in table:
        a, b, c, result = entry
        if result == 1:
            minterms.append((a, b, c))
        else:
            maxterms.append((a, b, c))
    
    minterm_str = ""
    for term in minterms:
        minterm_str += "("
        for i in range(3):
            if term[i]:
                minterm_str += chr(97+i)
            else:
                minterm_str += chr(97+i) + "'"
            if i < 2:
                minterm_str += " AND "
        minterm_str += ") OR "
    minterm_str = minterm_str[:-4]

    maxterm_str = ""
    for term in maxterms:
        maxterm_str += "("
        for i in range(3):
            if not term[i]:
                maxterm_str += chr(97+i)
            else:
                maxterm_str += chr(97+i) + "'"
            if i < 2:
                maxterm_str += " OR "
        maxterm_str += ") AND "
    maxterm_str = maxterm_str[:-5]
    
    return minterm_str, maxterm_str

def main():
    table = truth_table()
    print("Table de vérité:")
    print("a b c | f(a, b, c)")
    print("------------------")
    for entry in table:
        a, b, c, result = entry
        print(f"{a} {b} {c} | {result}")
    
    minterm, maxterm = canonical_forms(table)
    print("\nForme canonique (première forme):")
    print(minterm)
    print("\nForme canonique (seconde forme):")
    print(maxterm)

if __name__ == "__main__":
    main()
