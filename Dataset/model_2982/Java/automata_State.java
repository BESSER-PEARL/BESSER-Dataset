





import java.util.List;
import java.util.ArrayList;

public class automata_State  {

    private String name;
    private boolean initial;





    private automata_Automaton automata_automaton;


    public automata_State(
        String name,        boolean initial    ) {
        this.name = name;
        this.initial = initial;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getInitial() {
        return initial;
    }

    public void setInitial(boolean initial) {
        this.initial = initial;
    }

    public automata_Automaton getAutomata_automaton() {
        return automata_automaton;
    }

    public void setAutomata_automaton(automata_Automaton automata_automaton) {
        this.automata_automaton = automata_automaton;
    }

}