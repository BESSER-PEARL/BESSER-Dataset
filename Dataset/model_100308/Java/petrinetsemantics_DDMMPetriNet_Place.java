





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_DDMMPetriNet_Place extends Node {

    private int initialMarking;



    public petrinetsemantics_DDMMPetriNet_Place(
        int initialMarking    ) {
        super(
        );
        this.initialMarking = initialMarking;
    }


    public int getInitialmarking() {
        return initialMarking;
    }

    public void setInitialmarking(int initialMarking) {
        this.initialMarking = initialMarking;
    }


}