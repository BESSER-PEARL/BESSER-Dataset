





import java.util.List;
import java.util.ArrayList;

public class petrinetsemantics_DDMMPetriNet_Node  {

    private String name;





    private List<Arc> arcs;




    private List<Arc> arcs;


    public petrinetsemantics_DDMMPetriNet_Node(
        String name    ) {
        this.name = name;
        this.arcs = new ArrayList<>();
        this.arcs = new ArrayList<>();
    }

    public petrinetsemantics_DDMMPetriNet_Node(
        String name        ArrayList<Arc> arcs,        ArrayList<Arc> arcs    ) {
        this.name = name;
        this.arcs = arcs;
        this.arcs = arcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Arc> getArcs() {
        return arcs;
    }

    public void addArc(Arc arc) {
        this.arcs.add(arc);
    }
    public List<Arc> getArcs() {
        return arcs;
    }

    public void addArc(Arc arc) {
        this.arcs.add(arc);
    }

}