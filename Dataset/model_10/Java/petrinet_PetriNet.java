





import java.util.List;
import java.util.ArrayList;

public class petrinet_PetriNet  {

    private String name;





    private List<petrinet_Arc> petrinet_arcs;




    private petrinet_Arc petrinet_arc;


    public petrinet_PetriNet(
        String name    ) {
        this.name = name;
        this.petrinet_arcs = new ArrayList<>();
    }

    public petrinet_PetriNet(
        String name        ArrayList<petrinet_Arc> petrinet_arcs    ) {
        this.name = name;
        this.petrinet_arcs = petrinet_arcs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<petrinet_Arc> getPetrinet_arcs() {
        return petrinet_arcs;
    }

    public void addPetrinet_arc(Petrinet_arc petrinet_arc) {
        this.petrinet_arcs.add(petrinet_arc);
    }
    public petrinet_Arc getPetrinet_arc() {
        return petrinet_arc;
    }

    public void setPetrinet_arc(petrinet_Arc petrinet_arc) {
        this.petrinet_arc = petrinet_arc;
    }

}