





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_SDMMPetriNet_Place_dynamic extends Node_dynamic {

    private int marking;



    public petrinetsemantics_SDMMPetriNet_Place_dynamic(
        int marking    ) {
        super(
        );
        this.marking = marking;
    }


    public int getMarking() {
        return marking;
    }

    public void setMarking(int marking) {
        this.marking = marking;
    }


}