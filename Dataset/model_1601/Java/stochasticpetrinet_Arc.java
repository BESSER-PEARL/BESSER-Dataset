





import java.util.List;
import java.util.ArrayList;

public class stochasticpetrinet_Arc  {

    private String kind;





    private stochasticpetrinet_Place stochasticpetrinet_place;




    private stochasticpetrinet_Transition stochasticpetrinet_transition;




    private stochasticpetrinet_Transition stochasticpetrinet_transition;


    public stochasticpetrinet_Arc(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public stochasticpetrinet_Place getStochasticpetrinet_place() {
        return stochasticpetrinet_place;
    }

    public void setStochasticpetrinet_place(stochasticpetrinet_Place stochasticpetrinet_place) {
        this.stochasticpetrinet_place = stochasticpetrinet_place;
    }
    public stochasticpetrinet_Transition getStochasticpetrinet_transition() {
        return stochasticpetrinet_transition;
    }

    public void setStochasticpetrinet_transition(stochasticpetrinet_Transition stochasticpetrinet_transition) {
        this.stochasticpetrinet_transition = stochasticpetrinet_transition;
    }
    public stochasticpetrinet_Transition getStochasticpetrinet_transition() {
        return stochasticpetrinet_transition;
    }

    public void setStochasticpetrinet_transition(stochasticpetrinet_Transition stochasticpetrinet_transition) {
        this.stochasticpetrinet_transition = stochasticpetrinet_transition;
    }

}