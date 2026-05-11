





import java.util.List;
import java.util.ArrayList;

public class automata_Variable  {

    private String name;





    private automata_Automaton automata_automaton;


    public automata_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public automata_Automaton getAutomata_automaton() {
        return automata_automaton;
    }

    public void setAutomata_automaton(automata_Automaton automata_automaton) {
        this.automata_automaton = automata_automaton;
    }

}