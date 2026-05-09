





import java.util.List;
import java.util.ArrayList;

public class ea_automata_Transition extends ExtendibleElement {

    private String id;





    private Automaton automaton;


    public ea_automata_Transition(
        String id    ) {
        super(
        );
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public Automaton getAutomaton() {
        return automaton;
    }

    public void setAutomaton(Automaton automaton) {
        this.automaton = automaton;
    }

}