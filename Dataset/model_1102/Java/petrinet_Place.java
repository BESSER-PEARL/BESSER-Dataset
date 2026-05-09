





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends NamedElement {






    private petrinet_Transition petrinet_transition;




    private List<petrinet_Transition> petrinet_transitions;




    private List<petrinet_Transition> petrinet_transitions;




    private petrinet_Net petrinet_net;




    private petrinet_Transition petrinet_transition;




    private petrinet_Net petrinet_net;


    public petrinet_Place(
    ) {
        super(
        );
        this.petrinet_transitions = new ArrayList<>();
        this.petrinet_transitions = new ArrayList<>();
    }

    public petrinet_Place(
        ArrayList<petrinet_Transition> petrinet_transitions,        ArrayList<petrinet_Transition> petrinet_transitions    ) {
        this.petrinet_transitions = petrinet_transitions;
        this.petrinet_transitions = petrinet_transitions;
    }


    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public petrinet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(petrinet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }
    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }
    public petrinet_Net getPetrinet_net() {
        return petrinet_net;
    }

    public void setPetrinet_net(petrinet_Net petrinet_net) {
        this.petrinet_net = petrinet_net;
    }

}