





import java.util.List;
import java.util.ArrayList;

public class fuzzyAutomaton_Input extends Action {






    private List<fuzzyAutomaton_Variable> fuzzyautomaton_variables;


    public fuzzyAutomaton_Input(
    ) {
        super(
        );
        this.fuzzyautomaton_variables = new ArrayList<>();
    }

    public fuzzyAutomaton_Input(
        ArrayList<fuzzyAutomaton_Variable> fuzzyautomaton_variables    ) {
        this.fuzzyautomaton_variables = fuzzyautomaton_variables;
    }


    public List<fuzzyAutomaton_Variable> getFuzzyautomaton_variables() {
        return fuzzyautomaton_variables;
    }

    public void addFuzzyautomaton_variable(Fuzzyautomaton_variable fuzzyautomaton_variable) {
        this.fuzzyautomaton_variables.add(fuzzyautomaton_variable);
    }

}