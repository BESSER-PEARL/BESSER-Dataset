





import java.util.List;
import java.util.ArrayList;

public class automaton_Transition extends NamedElement {






    private automaton_Automaton automaton_automaton;




    private automaton_State automaton_state;




    private List<automaton_Output> automaton_outputs;




    private automaton_State automaton_state;


    public automaton_Transition(
    ) {
        super(
        );
        this.automaton_outputs = new ArrayList<>();
    }

    public automaton_Transition(
        ArrayList<automaton_Output> automaton_outputs    ) {
        this.automaton_outputs = automaton_outputs;
    }


    public automaton_Automaton getAutomaton_automaton() {
        return automaton_automaton;
    }

    public void setAutomaton_automaton(automaton_Automaton automaton_automaton) {
        this.automaton_automaton = automaton_automaton;
    }
    public automaton_State getAutomaton_state() {
        return automaton_state;
    }

    public void setAutomaton_state(automaton_State automaton_state) {
        this.automaton_state = automaton_state;
    }
    public List<automaton_Output> getAutomaton_outputs() {
        return automaton_outputs;
    }

    public void addAutomaton_output(Automaton_output automaton_output) {
        this.automaton_outputs.add(automaton_output);
    }
    public automaton_State getAutomaton_state() {
        return automaton_state;
    }

    public void setAutomaton_state(automaton_State automaton_state) {
        this.automaton_state = automaton_state;
    }

}