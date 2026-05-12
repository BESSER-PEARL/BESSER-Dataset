





import java.util.List;
import java.util.ArrayList;

public class pnmlcoremodel_Node extends PnObject {






    private pnmlcoremodel_Arc pnmlcoremodel_arc;




    private List<pnmlcoremodel_Arc> pnmlcoremodel_arcs;




    private pnmlcoremodel_Arc pnmlcoremodel_arc;




    private List<pnmlcoremodel_Arc> pnmlcoremodel_arcs;


    public pnmlcoremodel_Node(
    ) {
        super(
        );
        this.pnmlcoremodel_arcs = new ArrayList<>();
        this.pnmlcoremodel_arcs = new ArrayList<>();
    }

    public pnmlcoremodel_Node(
        ArrayList<pnmlcoremodel_Arc> pnmlcoremodel_arcs,        ArrayList<pnmlcoremodel_Arc> pnmlcoremodel_arcs    ) {
        this.pnmlcoremodel_arcs = pnmlcoremodel_arcs;
        this.pnmlcoremodel_arcs = pnmlcoremodel_arcs;
    }


    public pnmlcoremodel_Arc getPnmlcoremodel_arc() {
        return pnmlcoremodel_arc;
    }

    public void setPnmlcoremodel_arc(pnmlcoremodel_Arc pnmlcoremodel_arc) {
        this.pnmlcoremodel_arc = pnmlcoremodel_arc;
    }
    public List<pnmlcoremodel_Arc> getPnmlcoremodel_arcs() {
        return pnmlcoremodel_arcs;
    }

    public void addPnmlcoremodel_arc(Pnmlcoremodel_arc pnmlcoremodel_arc) {
        this.pnmlcoremodel_arcs.add(pnmlcoremodel_arc);
    }
    public pnmlcoremodel_Arc getPnmlcoremodel_arc() {
        return pnmlcoremodel_arc;
    }

    public void setPnmlcoremodel_arc(pnmlcoremodel_Arc pnmlcoremodel_arc) {
        this.pnmlcoremodel_arc = pnmlcoremodel_arc;
    }
    public List<pnmlcoremodel_Arc> getPnmlcoremodel_arcs() {
        return pnmlcoremodel_arcs;
    }

    public void addPnmlcoremodel_arc(Pnmlcoremodel_arc pnmlcoremodel_arc) {
        this.pnmlcoremodel_arcs.add(pnmlcoremodel_arc);
    }

}