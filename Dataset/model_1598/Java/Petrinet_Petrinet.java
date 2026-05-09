





import java.util.List;
import java.util.ArrayList;

public class Petrinet_Petrinet  {






    private List<Petrinet_Element> petrinet_elements;


    public Petrinet_Petrinet(
    ) {
        this.petrinet_elements = new ArrayList<>();
    }

    public Petrinet_Petrinet(
        ArrayList<Petrinet_Element> petrinet_elements    ) {
        this.petrinet_elements = petrinet_elements;
    }


    public List<Petrinet_Element> getPetrinet_elements() {
        return petrinet_elements;
    }

    public void addPetrinet_element(Petrinet_element petrinet_element) {
        this.petrinet_elements.add(petrinet_element);
    }

}