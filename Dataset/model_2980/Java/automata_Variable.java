





import java.util.List;
import java.util.ArrayList;

public class automata_Variable  {

    private String name;
    private String type;





    private automata_Automaton automata_automaton;


    public automata_Variable(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public automata_Automaton getAutomata_automaton() {
        return automata_automaton;
    }

    public void setAutomata_automaton(automata_Automaton automata_automaton) {
        this.automata_automaton = automata_automaton;
    }

}