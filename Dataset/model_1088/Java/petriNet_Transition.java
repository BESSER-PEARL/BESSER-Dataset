





import java.util.List;
import java.util.ArrayList;

public class petriNet_Transition extends Node {






    private petriNet_Place petrinet_place;


    public petriNet_Transition(
    ) {
        super(
        );
    }



    public petriNet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petriNet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }

}