from matplotlib import pyplot as plt
import escher

substrate_name_to_rxn = {'D-Glucose': 'EX_glc__D_e',
                         'L-Glutamate': 'EX_glu__L_e',
                         'L-Glutamine': 'EX_gln__L_e',
                         'D-Ribose': 'EX_rib__D_e',
                         'L-Lysine': 'EX_lys__L_e',
                         'D-Lactate': 'EX_lac__D_e',
                         'L-Aspartate': 'EX_asp__L_e',
                         'Formate': 'EX_for_e',
                         'Adenosine': 'EX_adn_e',
                         'Acetate': 'EX_ac_e'}

rxn_to_carbon_source = {v: i for i, v in substrate_name_to_rxn.items()}

plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 15
plt.rcParams['axes.labelsize'] = 15
plt.rcParams['axes.titlesize'] = 15


def plot_theoretical_yields(yield_list, substrate_list, target, rxn_count=list()):

    plt.figure(figsize=(6, 5))

    plt.bar(list(range(0, len(yield_list))), yield_list)

    plt.xticks(list(range(0, len(yield_list))), substrate_list,
               rotation=45, ha='right')
    if rxn_count:
        for i, (c_yield, rxn) in enumerate(zip(yield_list, rxn_count)):
            plt.text(i, c_yield + c_yield/100, rxn, ha='center', va='bottom', size=14)

    max_val = max(yield_list)
    plt.ylim([0, max_val + max_val/10])
    plt.ylabel(r'%s yield' % target)
    plt.title('Potential to produce %s \n by carbon substrate' % target)
    plt.tight_layout()


def visualize_flux(reaction_fluxes):
    builder = escher.Builder(map_name='iJO1366.Central metabolism',
                             reaction_scale=[
                                 {'type': 'min', 'color': '#cccccc',
                                  'size': 4},
                                 {'type': 'value', 'value': .01,
                                  'color': '#0000dd', 'size': 20},
                                 {'type': 'max', 'color': '#0000dd',
                                  'size': 20}])
    builder.reaction_data = reaction_fluxes.to_dict()

    return builder.display_in_notebook()

