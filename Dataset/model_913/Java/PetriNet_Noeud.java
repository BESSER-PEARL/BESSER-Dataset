





import java.util.List;
import java.util.ArrayList;

public class PetriNet_Noeud extends PetriElement {

    private String name;





    private PetriNet_Arc petrinet_arc;




    private List<PetriNet_Arc> petrinet_arcs;




    private List<PetriNet_Arc> petrinet_arcs;




    private PetriNet_Arc petrinet_arc;


    public PetriNet_Noeud(
        String name    ) {
        super(
        );
        this.name = name;
        this.petrinet_arcs = new ArrayList<>();
        this.petrinet_arcs = new ArrayList<>();
    }

    public PetriNet_Noeud(
        String name        ArrayList<PetriNet_Arc> petrinet_arcs,        ArrayList<PetriNet_Arc> petrinet_arcs    ) {
        this.name = name;
        this.petrinet_arcs = petrinet_arcs;
        this.petrinet_arcs = petrinet_arcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PetriNet_Arc getPetrinet_arc() {
        return petrinet_arc;
    }

    public void setPetrinet_arc(PetriNet_Arc petrinet_arc) {
        this.petrinet_arc = petrinet_arc;
    }
    public List<PetriNet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public List<PetriNet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public PetriNet_Arc getPetrinet_arc() {
        return petrinet_arc;
    }

    public void setPetrinet_arc(PetriNet_Arc petrinet_arc) {
        this.petrinet_arc = petrinet_arc;
    }

}