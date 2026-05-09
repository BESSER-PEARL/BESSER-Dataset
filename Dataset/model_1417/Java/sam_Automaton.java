





import java.util.List;
import java.util.ArrayList;

public class sam_Automaton extends ModelContent {






    private sam_Transition sam_transition;




    private sam_Port sam_port;




    private sam_AbstractState sam_abstractstate;




    private List<sam_Port> sam_ports;




    private sam_Automaton sam_automaton;




    private List<sam_AbstractState> sam_abstractstates;




    private List<sam_Transition> sam_transitions;


    public sam_Automaton(
    ) {
        super(
        );
        this.sam_ports = new ArrayList<>();
        this.sam_abstractstates = new ArrayList<>();
        this.sam_transitions = new ArrayList<>();
    }

    public sam_Automaton(
        ArrayList<sam_Port> sam_ports,        ArrayList<sam_AbstractState> sam_abstractstates,        ArrayList<sam_Transition> sam_transitions    ) {
        this.sam_ports = sam_ports;
        this.sam_abstractstates = sam_abstractstates;
        this.sam_transitions = sam_transitions;
    }


    public sam_Transition getSam_transition() {
        return sam_transition;
    }

    public void setSam_transition(sam_Transition sam_transition) {
        this.sam_transition = sam_transition;
    }
    public sam_Port getSam_port() {
        return sam_port;
    }

    public void setSam_port(sam_Port sam_port) {
        this.sam_port = sam_port;
    }
    public sam_AbstractState getSam_abstractstate() {
        return sam_abstractstate;
    }

    public void setSam_abstractstate(sam_AbstractState sam_abstractstate) {
        this.sam_abstractstate = sam_abstractstate;
    }
    public List<sam_Port> getSam_ports() {
        return sam_ports;
    }

    public void addSam_port(Sam_port sam_port) {
        this.sam_ports.add(sam_port);
    }
    public sam_Automaton getSam_automaton() {
        return sam_automaton;
    }

    public void setSam_automaton(sam_Automaton sam_automaton) {
        this.sam_automaton = sam_automaton;
    }
    public List<sam_AbstractState> getSam_abstractstates() {
        return sam_abstractstates;
    }

    public void addSam_abstractstate(Sam_abstractstate sam_abstractstate) {
        this.sam_abstractstates.add(sam_abstractstate);
    }
    public List<sam_Transition> getSam_transitions() {
        return sam_transitions;
    }

    public void addSam_transition(Sam_transition sam_transition) {
        this.sam_transitions.add(sam_transition);
    }

}