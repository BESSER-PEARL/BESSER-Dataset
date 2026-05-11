





import java.util.List;
import java.util.ArrayList;

public class interaction_AbstractCapability extends AbstractFunctionalChainContainer, Structure, CapellaElement {






    private List<interaction_State> interaction_states;




    private List<interaction_FunctionalChain> interaction_functionalchains;




    private interaction_AbstractCapability interaction_abstractcapability;




    private List<interaction_AbstractFunction> interaction_abstractfunctions;




    private List<interaction_AbstractCapability> interaction_abstractcapabilitys;




    private interaction_Constraint interaction_constraint;




    private List<interaction_Scenario> interaction_scenarios;




    private interaction_AbstractCapability interaction_abstractcapability;




    private interaction_Constraint interaction_constraint;


    public interaction_AbstractCapability(
    ) {
        super(
        );
        this.interaction_states = new ArrayList<>();
        this.interaction_functionalchains = new ArrayList<>();
        this.interaction_abstractfunctions = new ArrayList<>();
        this.interaction_abstractcapabilitys = new ArrayList<>();
        this.interaction_scenarios = new ArrayList<>();
    }

    public interaction_AbstractCapability(
        ArrayList<interaction_State> interaction_states,        ArrayList<interaction_FunctionalChain> interaction_functionalchains,        ArrayList<interaction_AbstractFunction> interaction_abstractfunctions,        ArrayList<interaction_AbstractCapability> interaction_abstractcapabilitys,        ArrayList<interaction_Scenario> interaction_scenarios    ) {
        this.interaction_states = interaction_states;
        this.interaction_functionalchains = interaction_functionalchains;
        this.interaction_abstractfunctions = interaction_abstractfunctions;
        this.interaction_abstractcapabilitys = interaction_abstractcapabilitys;
        this.interaction_scenarios = interaction_scenarios;
    }


    public List<interaction_State> getInteraction_states() {
        return interaction_states;
    }

    public void addInteraction_state(Interaction_state interaction_state) {
        this.interaction_states.add(interaction_state);
    }
    public List<interaction_FunctionalChain> getInteraction_functionalchains() {
        return interaction_functionalchains;
    }

    public void addInteraction_functionalchain(Interaction_functionalchain interaction_functionalchain) {
        this.interaction_functionalchains.add(interaction_functionalchain);
    }
    public interaction_AbstractCapability getInteraction_abstractcapability() {
        return interaction_abstractcapability;
    }

    public void setInteraction_abstractcapability(interaction_AbstractCapability interaction_abstractcapability) {
        this.interaction_abstractcapability = interaction_abstractcapability;
    }
    public List<interaction_AbstractFunction> getInteraction_abstractfunctions() {
        return interaction_abstractfunctions;
    }

    public void addInteraction_abstractfunction(Interaction_abstractfunction interaction_abstractfunction) {
        this.interaction_abstractfunctions.add(interaction_abstractfunction);
    }
    public List<interaction_AbstractCapability> getInteraction_abstractcapabilitys() {
        return interaction_abstractcapabilitys;
    }

    public void addInteraction_abstractcapability(Interaction_abstractcapability interaction_abstractcapability) {
        this.interaction_abstractcapabilitys.add(interaction_abstractcapability);
    }
    public interaction_Constraint getInteraction_constraint() {
        return interaction_constraint;
    }

    public void setInteraction_constraint(interaction_Constraint interaction_constraint) {
        this.interaction_constraint = interaction_constraint;
    }
    public List<interaction_Scenario> getInteraction_scenarios() {
        return interaction_scenarios;
    }

    public void addInteraction_scenario(Interaction_scenario interaction_scenario) {
        this.interaction_scenarios.add(interaction_scenario);
    }
    public interaction_AbstractCapability getInteraction_abstractcapability() {
        return interaction_abstractcapability;
    }

    public void setInteraction_abstractcapability(interaction_AbstractCapability interaction_abstractcapability) {
        this.interaction_abstractcapability = interaction_abstractcapability;
    }
    public interaction_Constraint getInteraction_constraint() {
        return interaction_constraint;
    }

    public void setInteraction_constraint(interaction_Constraint interaction_constraint) {
        this.interaction_constraint = interaction_constraint;
    }

}