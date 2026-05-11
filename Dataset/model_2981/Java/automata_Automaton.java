





import java.util.List;
import java.util.ArrayList;

public class automata_Automaton  {






    private List<automata_Variable> automata_variables;




    private List<automata_Transition> automata_transitions;


    public automata_Automaton(
    ) {
        this.automata_variables = new ArrayList<>();
        this.automata_transitions = new ArrayList<>();
    }

    public automata_Automaton(
        ArrayList<automata_Variable> automata_variables,        ArrayList<automata_Transition> automata_transitions    ) {
        this.automata_variables = automata_variables;
        this.automata_transitions = automata_transitions;
    }


    public List<automata_Variable> getAutomata_variables() {
        return automata_variables;
    }

    public void addAutomata_variable(Automata_variable automata_variable) {
        this.automata_variables.add(automata_variable);
    }
    public List<automata_Transition> getAutomata_transitions() {
        return automata_transitions;
    }

    public void addAutomata_transition(Automata_transition automata_transition) {
        this.automata_transitions.add(automata_transition);
    }

}