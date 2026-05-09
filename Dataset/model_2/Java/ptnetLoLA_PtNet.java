





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_PtNet  {






    private List<ptnetLoLA_Transition> ptnetlola_transitions;




    private List<ptnetLoLA_Place> ptnetlola_places;




    private ptnetLoLA_Annotation ptnetlola_annotation;


    public ptnetLoLA_PtNet(
    ) {
        this.ptnetlola_transitions = new ArrayList<>();
        this.ptnetlola_places = new ArrayList<>();
    }

    public ptnetLoLA_PtNet(
        ArrayList<ptnetLoLA_Transition> ptnetlola_transitions,        ArrayList<ptnetLoLA_Place> ptnetlola_places    ) {
        this.ptnetlola_transitions = ptnetlola_transitions;
        this.ptnetlola_places = ptnetlola_places;
    }


    public List<ptnetLoLA_Transition> getPtnetlola_transitions() {
        return ptnetlola_transitions;
    }

    public void addPtnetlola_transition(Ptnetlola_transition ptnetlola_transition) {
        this.ptnetlola_transitions.add(ptnetlola_transition);
    }
    public List<ptnetLoLA_Place> getPtnetlola_places() {
        return ptnetlola_places;
    }

    public void addPtnetlola_place(Ptnetlola_place ptnetlola_place) {
        this.ptnetlola_places.add(ptnetlola_place);
    }
    public ptnetLoLA_Annotation getPtnetlola_annotation() {
        return ptnetlola_annotation;
    }

    public void setPtnetlola_annotation(ptnetLoLA_Annotation ptnetlola_annotation) {
        this.ptnetlola_annotation = ptnetlola_annotation;
    }

}