





import java.util.List;
import java.util.ArrayList;

public class PetriNetMM2_Arc extends PetriNetModelElement {

    private int weight;



    public PetriNetMM2_Arc(
        int weight    ) {
        super(
        );
        this.weight = weight;
    }


    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }


}