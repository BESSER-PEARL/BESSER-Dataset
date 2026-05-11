





import java.util.List;
import java.util.ArrayList;

public class interaction_Scenario extends AbstractBehavior, Namespace {

    private String kind;
    private boolean merged;





    private List<interaction_Scenario> interaction_scenarios;




    private List<interaction_AbstractFunction> interaction_abstractfunctions;




    private List<interaction_Part> interaction_parts;




    private interaction_Scenario interaction_scenario;


    public interaction_Scenario(
        String kind,        boolean merged    ) {
        super(
        );
        this.kind = kind;
        this.merged = merged;
        this.interaction_scenarios = new ArrayList<>();
        this.interaction_abstractfunctions = new ArrayList<>();
        this.interaction_parts = new ArrayList<>();
    }

    public interaction_Scenario(
        String kind,        boolean merged        ArrayList<interaction_Scenario> interaction_scenarios,        ArrayList<interaction_AbstractFunction> interaction_abstractfunctions,        ArrayList<interaction_Part> interaction_parts    ) {
        this.kind = kind;
        this.merged = merged;
        this.interaction_scenarios = interaction_scenarios;
        this.interaction_abstractfunctions = interaction_abstractfunctions;
        this.interaction_parts = interaction_parts;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public boolean getMerged() {
        return merged;
    }

    public void setMerged(boolean merged) {
        this.merged = merged;
    }

    public List<interaction_Scenario> getInteraction_scenarios() {
        return interaction_scenarios;
    }

    public void addInteraction_scenario(Interaction_scenario interaction_scenario) {
        this.interaction_scenarios.add(interaction_scenario);
    }
    public List<interaction_AbstractFunction> getInteraction_abstractfunctions() {
        return interaction_abstractfunctions;
    }

    public void addInteraction_abstractfunction(Interaction_abstractfunction interaction_abstractfunction) {
        this.interaction_abstractfunctions.add(interaction_abstractfunction);
    }
    public List<interaction_Part> getInteraction_parts() {
        return interaction_parts;
    }

    public void addInteraction_part(Interaction_part interaction_part) {
        this.interaction_parts.add(interaction_part);
    }
    public interaction_Scenario getInteraction_scenario() {
        return interaction_scenario;
    }

    public void setInteraction_scenario(interaction_Scenario interaction_scenario) {
        this.interaction_scenario = interaction_scenario;
    }

}