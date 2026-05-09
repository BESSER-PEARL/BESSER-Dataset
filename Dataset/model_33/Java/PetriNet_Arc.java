





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc extends NamedElement {

    private int weight;



    public PetriNet_Arc(
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