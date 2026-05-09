





import java.util.List;
import java.util.ArrayList;

public class petrinet_Net  {






    private List<petrinet_Box> petrinet_boxs;




    private List<petrinet_Transition> petrinet_transitions;




    private List<petrinet_Place> petrinet_places;


    public petrinet_Net(
    ) {
        this.petrinet_boxs = new ArrayList<>();
        this.petrinet_transitions = new ArrayList<>();
        this.petrinet_places = new ArrayList<>();
    }

    public petrinet_Net(
        ArrayList<petrinet_Box> petrinet_boxs,        ArrayList<petrinet_Transition> petrinet_transitions,        ArrayList<petrinet_Place> petrinet_places    ) {
        this.petrinet_boxs = petrinet_boxs;
        this.petrinet_transitions = petrinet_transitions;
        this.petrinet_places = petrinet_places;
    }


    public List<petrinet_Box> getPetrinet_boxs() {
        return petrinet_boxs;
    }

    public void addPetrinet_box(Petrinet_box petrinet_box) {
        this.petrinet_boxs.add(petrinet_box);
    }
    public List<petrinet_Transition> getPetrinet_transitions() {
        return petrinet_transitions;
    }

    public void addPetrinet_transition(Petrinet_transition petrinet_transition) {
        this.petrinet_transitions.add(petrinet_transition);
    }
    public List<petrinet_Place> getPetrinet_places() {
        return petrinet_places;
    }

    public void addPetrinet_place(Petrinet_place petrinet_place) {
        this.petrinet_places.add(petrinet_place);
    }

}