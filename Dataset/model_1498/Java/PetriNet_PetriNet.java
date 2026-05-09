





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PetriNet  {

    private String name;





    private List<PetriNet_Arc> petrinet_arcs;




    private List<PetriNet_PetriElement> petrinet_petrielements;


    public PetriNet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_arcs = new ArrayList<>();
        this.petrinet_petrielements = new ArrayList<>();
    }

    public PetriNet_PetriNet(
        String name        ArrayList<PetriNet_Arc> petrinet_arcs,        ArrayList<PetriNet_PetriElement> petrinet_petrielements    ) {
        this.name = name;
        this.petrinet_arcs = petrinet_arcs;
        this.petrinet_petrielements = petrinet_petrielements;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PetriNet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public List<PetriNet_PetriElement> getPetrinet_petrielements() {
        return petrinet_petrielements;
    }

    public void addPetrinet_petrielement(Petrinet_petrielement petrinet_petrielement) {
        this.petrinet_petrielements.add(petrinet_petrielement);
    }

}