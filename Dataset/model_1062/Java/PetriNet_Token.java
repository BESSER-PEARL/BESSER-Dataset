





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Token  {

    private String values;





    private PetriNet_Place petrinet_place;


    public PetriNet_Token(
        String values    ) {
        this.values = values;
    }


    public String getValues() {
        return values;
    }

    public void setValues(String values) {
        this.values = values;
    }

    public PetriNet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(PetriNet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }

}