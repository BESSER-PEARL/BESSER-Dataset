





import java.util.List;
import java.util.ArrayList;

public class petriNet_PetriNetwork  {

    private String name;





    private List<petriNet_PetriElement> petrinet_petrielements;


    public petriNet_PetriNetwork(
        String name    ) {
        this.name = name;
        this.petrinet_petrielements = new ArrayList<>();
    }

    public petriNet_PetriNetwork(
        String name        ArrayList<petriNet_PetriElement> petrinet_petrielements    ) {
        this.name = name;
        this.petrinet_petrielements = petrinet_petrielements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petriNet_PetriElement> getPetrinet_petrielements() {
        return petrinet_petrielements;
    }

    public void addPetrinet_petrielement(Petrinet_petrielement petrinet_petrielement) {
        this.petrinet_petrielements.add(petrinet_petrielement);
    }

}