import cobra.test
ijo = cobra.test.create_test_model('ecoli')

reactions = ['HEX1', 'PGI', 'PFK', 'TPI', 'FBA',
             'GAPD', 'PGK', 'PGM', 'ENO', 'PYK']

reactions_and_info = {}
for r in reactions:
    r_obj = ijo.reactions.get_by_id(r)
    reactions_and_info[r] = {}
    reactions_and_info[r]['stoichiometry'] = \
        {i.id: v for i, v in r_obj.metabolites.items()}

    reactions_and_info[r]['upper_bound'] = r_obj.upper_bound
    reactions_and_info[r]['lower_bound'] = r_obj.lower_bound
    reactions_and_info[r]['name'] = r_obj.name
    reactions_and_info[r]['gene_reaction_rule'] = r_obj.gene_reaction_rule

print(reactions_and_info)

mets_and_info = {}
for r in reactions_and_info:
    for met in reactions_and_info[r]['stoichiometry']:
        mets_and_info[met] = {}
        met_obj = ijo.metabolites.get_by_id(met)

        mets_and_info[met]['name'] = met_obj.name
        mets_and_info[met]['formula'] = met_obj.formula
        mets_and_info[met]['charge'] = met_obj.charge
        mets_and_info[met]['compartment'] = met_obj.compartment

print(mets_and_info)