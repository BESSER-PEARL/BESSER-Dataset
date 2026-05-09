





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {






    private List<petrinet_Element> petrinet_elements;


    public petrinet_PetriNet(
    ) {
        this.petrinet_elements = new ArrayList<>();
    }

    public petrinet_PetriNet(
        ArrayList<petrinet_Element> petrinet_elements    ) {
        this.petrinet_elements = petrinet_elements;
    }


    public List<petrinet_Element> getPetrinet_elements() {
        return petrinet_elements;
    }

    public void addPetrinet_element(Petrinet_element petrinet_element) {
        this.petrinet_elements.add(petrinet_element);
    }

}