





import java.util.List;
import java.util.ArrayList;

public class org.k1s.nppn_Page extends HasName, HasLabel {






    private List<nppn_Arc> nppn_arcs;


    public org.k1s.nppn_Page(
    ) {
        super(
        );
        this.nppn_arcs = new ArrayList<>();
    }

    public org.k1s.nppn_Page(
        ArrayList<nppn_Arc> nppn_arcs    ) {
        this.nppn_arcs = nppn_arcs;
    }


    public List<nppn_Arc> getNppn_arcs() {
        return nppn_arcs;
    }

    public void addNppn_arc(Nppn_arc nppn_arc) {
        this.nppn_arcs.add(nppn_arc);
    }

}