





import java.util.List;
import java.util.ArrayList;

public class petrinet_Place extends Noeud {

    private int marking;



    public petrinet_Place(
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