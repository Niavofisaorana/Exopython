from itertools import product

def evaluate_expression(expression, variable_values):
    # Évalue une expression booléenne avec des valeurs de variables spécifiques
    env = {var: val for var, val in variable_values.items()}
    return eval(expression, env)

def generate_truth_table(expression, variables):
    # Génère la table de vérité pour une expression booléenne donnée
    table = []
    num_vars = len(variables)
    for values in product([0, 1], repeat=num_vars):
        variable_values = dict(zip(variables, values))
        result = evaluate_expression(expression, variable_values)
        table.append({**variable_values, 'result': result})
    return table

def get_canonical_forms(truth_table):
    true_terms = []
    false_terms = []
    
    for row in truth_table:
        term = []
        for var, val in row.items():
            if var != 'result':
                if val == 1:
                    term.append(f"({var})")
                else:
                    term.append(f"~({var})")
        if row['result']:
            true_terms.append(" & ".join(term))
        else:
            false_terms.append(" | ".join(term))
    
    first_canonical = " | ".join(true_terms)
    second_canonical = " & ".join(false_terms)
    
    return first_canonical, second_canonical

def main():
    expression = input("Entrez une expression logique en utilisant les opérateurs logiques (& pour ET, | pour OU, ~ pour NON) : ")
    variables = set([char for char in expression if char.isalpha()])
    
    truth_table = generate_truth_table(expression, variables)
    
    print("\nTable de vérité :")
    headers = sorted(variables) + ['result']
    for header in headers:
        print(header, end='\t')
    print()
    
    for row in truth_table:
        for var in headers:
            print(row[var], end='\t')
        print()
    
    first_canonical, second_canonical = get_canonical_forms(truth_table)
    
    print("\nPremière forme canonique :")
    print(first_canonical)
    
    print("\nDeuxième forme canonique :")
    print(second_canonical)

if __name__ == "__main__":
    main()