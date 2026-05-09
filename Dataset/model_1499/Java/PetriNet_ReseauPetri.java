





import java.util.List;
import java.util.ArrayList;

public class PetriNet_ReseauPetri  {

    private String name;





    private List<PetriNet_PetriElement> petrinet_petrielements;




    private List<PetriNet_Arc> petrinet_arcs;


    public PetriNet_ReseauPetri(
        String name    ) {
        this.name = name;
        this.petrinet_petrielements = new ArrayList<>();
        this.petrinet_arcs = new ArrayList<>();
    }

    public PetriNet_ReseauPetri(
        String name        ArrayList<PetriNet_PetriElement> petrinet_petrielements,        ArrayList<PetriNet_Arc> petrinet_arcs    ) {
        this.name = name;
        this.petrinet_petrielements = petrinet_petrielements;
        this.petrinet_arcs = petrinet_arcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<PetriNet_PetriElement> getPetrinet_petrielements() {
        return petrinet_petrielements;
    }

    public void addPetrinet_petrielement(Petrinet_petrielement petrinet_petrielement) {
        this.petrinet_petrielements.add(petrinet_petrielement);
    }
    public List<PetriNet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }

}