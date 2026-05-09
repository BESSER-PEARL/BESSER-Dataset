





import java.util.List;
import java.util.ArrayList;

public class lit_petriNets_Net  {






    private lit_petriNets_Place lit_petrinets_place;




    private List<lit_petriNets_Transition> lit_petrinets_transitions;




    private List<lit_petriNets_Place> lit_petrinets_places;




    private lit_petriNets_Transition lit_petrinets_transition;


    public lit_petriNets_Net(
    ) {
        this.lit_petrinets_transitions = new ArrayList<>();
        this.lit_petrinets_places = new ArrayList<>();
    }

    public lit_petriNets_Net(
        ArrayList<lit_petriNets_Transition> lit_petrinets_transitions,        ArrayList<lit_petriNets_Place> lit_petrinets_places    ) {
        this.lit_petrinets_transitions = lit_petrinets_transitions;
        this.lit_petrinets_places = lit_petrinets_places;
    }


    public lit_petriNets_Place getLit_petrinets_place() {
        return lit_petrinets_place;
    }

    public void setLit_petrinets_place(lit_petriNets_Place lit_petrinets_place) {
        this.lit_petrinets_place = lit_petrinets_place;
    }
    public List<lit_petriNets_Transition> getLit_petrinets_transitions() {
        return lit_petrinets_transitions;
    }

    public void addLit_petrinets_transition(Lit_petrinets_transition lit_petrinets_transition) {
        this.lit_petrinets_transitions.add(lit_petrinets_transition);
    }
    public List<lit_petriNets_Place> getLit_petrinets_places() {
        return lit_petrinets_places;
    }

    public void addLit_petrinets_place(Lit_petrinets_place lit_petrinets_place) {
        this.lit_petrinets_places.add(lit_petrinets_place);
    }
    public lit_petriNets_Transition getLit_petrinets_transition() {
        return lit_petrinets_transition;
    }

    public void setLit_petrinets_transition(lit_petriNets_Transition lit_petrinets_transition) {
        this.lit_petrinets_transition = lit_petrinets_transition;
    }

}