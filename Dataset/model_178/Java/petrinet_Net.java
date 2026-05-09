





import java.util.List;
import java.util.ArrayList;

public class petrinet_Net  {






    private List<petrinet_Place> petrinet_places;




    private List<petrinet_Transition> petrinet_transitions;




    private petrinet_NetStopEvent petrinet_netstopevent;


    public petrinet_Net(
    ) {
        this.petrinet_places = new ArrayList<>();
        this.petrinet_transitions = new ArrayList<>();
    }

    public petrinet_Net(
        ArrayList<petrinet_Place> petrinet_places,        ArrayList<petrinet_Transition> petrinet_transitions    ) {
        this.petrinet_places = petrinet_places;
        this.petrinet_transitions = petrinet_transitions;
    }


    public List<petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }
    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public petrinet_NetStopEvent getPetrinet_netstopevent() {
        return petrinet_netstopevent;
    }

    public void setPetrinet_netstopevent(petrinet_NetStopEvent petrinet_netstopevent) {
        this.petrinet_netstopevent = petrinet_netstopevent;
    }

}