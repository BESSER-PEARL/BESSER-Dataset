





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Arc extends NamedElement {

    private String weight;





    private PetriNet petrinet;


    public PetriNet_Arc(
        String weight    ) {
        super(
        );
        this.weight = weight;
    }


    public String getWeight() {
        return weight;
    }

    public void setWeight(String weight) {
        this.weight = weight;
    }

    public PetriNet getPetrinet() {
        return petrinet;
    }

    public void setPetrinet(PetriNet petrinet) {
        this.petrinet = petrinet;
    }

}