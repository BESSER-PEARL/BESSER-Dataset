





import java.util.List;
import java.util.ArrayList;

public class PetriNet_PetriNet extends NamedElement {






    private List<Arc> arcs;


    public PetriNet_PetriNet(
    ) {
        super(
        );
        this.arcs = new ArrayList<>();
    }

    public PetriNet_PetriNet(
        ArrayList<Arc> arcs    ) {
        this.arcs = arcs;
    }


    public List<Arc> getArcs() {
        return arcs;
    }

    public void addArc(Arc arc) {
        this.arcs.add(arc);
    }

}