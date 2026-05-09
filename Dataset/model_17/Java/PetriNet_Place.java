





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Place extends Node {

    private int marking;



    public PetriNet_Place(
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