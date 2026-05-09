





import java.util.List;
import java.util.ArrayList;

public class petrinet_OutputArc extends Arc {






    private petrinet_Place petrinet_place;




    private petrinet_Transition petrinet_transition;


    public petrinet_OutputArc(
    ) {
        super(
        );
    }



    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }
    public petrinet_Transition getPetrinet_transition() {
        return petrinet_transition;
    }

    public void setPetrinet_transition(petrinet_Transition petrinet_transition) {
        this.petrinet_transition = petrinet_transition;
    }

}