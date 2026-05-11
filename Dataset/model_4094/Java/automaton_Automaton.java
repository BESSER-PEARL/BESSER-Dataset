





import java.util.List;
import java.util.ArrayList;

public class automaton_Automaton extends NamedElement {






    private List<automaton_State> automaton_states;




    private List<automaton_Input> automaton_inputs;


    public automaton_Automaton(
    ) {
        super(
        );
        this.automaton_states = new ArrayList<>();
        this.automaton_inputs = new ArrayList<>();
    }

    public automaton_Automaton(
        ArrayList<automaton_State> automaton_states,        ArrayList<automaton_Input> automaton_inputs    ) {
        this.automaton_states = automaton_states;
        this.automaton_inputs = automaton_inputs;
    }


    public List<automaton_State> getAutomaton_states() {
        return automaton_states;
    }

    public void addAutomaton_state(Automaton_state automaton_state) {
        this.automaton_states.add(automaton_state);
    }
    public List<automaton_Input> getAutomaton_inputs() {
        return automaton_inputs;
    }

    public void addAutomaton_input(Automaton_input automaton_input) {
        this.automaton_inputs.add(automaton_input);
    }

}