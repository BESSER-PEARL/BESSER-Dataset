





import java.util.List;
import java.util.ArrayList;

public class org_k1s_nppn_Page extends HasLabel, HasName {






    private List<nppn_Arc> nppn_arcs;


    public org_k1s_nppn_Page(
    ) {
        super(
        );
        this.nppn_arcs = new ArrayList<>();
    }

    public org_k1s_nppn_Page(
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