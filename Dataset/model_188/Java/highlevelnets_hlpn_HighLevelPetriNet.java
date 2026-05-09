





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_hlpn_HighLevelPetriNet extends hlpn_ContextVariable, common_INetElement {






    private List<Arc> arcs;


    public highlevelnets_hlpn_HighLevelPetriNet(
    ) {
        super(
        );
        this.arcs = new ArrayList<>();
    }

    public highlevelnets_hlpn_HighLevelPetriNet(
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