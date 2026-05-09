





import java.util.List;
import java.util.ArrayList;

public class ea_automata_State extends ExtendibleElement {

    private String id;
    private String name;





    private List<Transition> transitions;




    private List<Transition> transitions;


    public ea_automata_State(
        String id,        String name    ) {
        super(
        );
        this.id = id;
        this.name = name;
        this.transitions = new ArrayList<>();
        this.transitions = new ArrayList<>();
    }

    public ea_automata_State(
        String id,        String name        ArrayList<Transition> transitions,        ArrayList<Transition> transitions    ) {
        this.id = id;
        this.name = name;
        this.transitions = transitions;
        this.transitions = transitions;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }
    public List<Transition> getTransitions() {
        return transitions;
    }

    public void addTransition(Transition transition) {
        this.transitions.add(transition);
    }

}