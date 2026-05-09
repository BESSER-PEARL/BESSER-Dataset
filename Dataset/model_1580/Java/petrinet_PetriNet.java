





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {

    private String name;





    private List<petrinet_Element> petrinet_elements;


    public petrinet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_elements = new ArrayList<>();
    }

    public petrinet_PetriNet(
        String name        ArrayList<petrinet_Element> petrinet_elements    ) {
        this.name = name;
        this.petrinet_elements = petrinet_elements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinet_Element> getPetrinet_elements() {
        return petrinet_elements;
    }

    public void addPetrinet_element(Petrinet_element petrinet_element) {
        this.petrinet_elements.add(petrinet_element);
    }

}