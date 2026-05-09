





import java.util.List;
import java.util.ArrayList;

public class PetriNet  {






    private PetriNet_Element petrinet_element;




    private PetriNet_Arc petrinet_arc;


    public PetriNet(
    ) {
    }



    public PetriNet_Element getPetrinet_element() {
        return petrinet_element;
    }

    public void setPetrinet_element(PetriNet_Element petrinet_element) {
        this.petrinet_element = petrinet_element;
    }
    public PetriNet_Arc getPetrinet_arc() {
        return petrinet_arc;
    }

    public void setPetrinet_arc(PetriNet_Arc petrinet_arc) {
        this.petrinet_arc = petrinet_arc;
    }

}