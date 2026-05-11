





import java.util.List;
import java.util.ArrayList;

public class automata_Automata  {






    private List<automata_State> automata_states;




    private List<automata_Final> automata_finals;




    private List<automata_Transition> automata_transitions;


    public automata_Automata(
    ) {
        this.automata_states = new ArrayList<>();
        this.automata_finals = new ArrayList<>();
        this.automata_transitions = new ArrayList<>();
    }

    public automata_Automata(
        ArrayList<automata_State> automata_states,        ArrayList<automata_Final> automata_finals,        ArrayList<automata_Transition> automata_transitions    ) {
        this.automata_states = automata_states;
        this.automata_finals = automata_finals;
        this.automata_transitions = automata_transitions;
    }


    public List<automata_State> getAutomata_states() {
        return automata_states;
    }

    public void addAutomata_state(Automata_state automata_state) {
        this.automata_states.add(automata_state);
    }
    public List<automata_Final> getAutomata_finals() {
        return automata_finals;
    }

    public void addAutomata_final(Automata_final automata_final) {
        this.automata_finals.add(automata_final);
    }
    public List<automata_Transition> getAutomata_transitions() {
        return automata_transitions;
    }

    public void addAutomata_transition(Automata_transition automata_transition) {
        this.automata_transitions.add(automata_transition);
    }

}