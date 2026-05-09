





import java.util.List;
import java.util.ArrayList;

public class apromore_Net  {

    private int ident;





    private apromore_CanonicalProcess apromore_canonicalprocess;




    private apromore_CanonicalProcess apromore_canonicalprocess;




    private apromore_Task apromore_task;




    private List<apromore_Edge> apromore_edges;


    public apromore_Net(
        int ident    ) {
        this.ident = ident;
        this.apromore_edges = new ArrayList<>();
    }

    public apromore_Net(
        int ident        ArrayList<apromore_Edge> apromore_edges    ) {
        this.ident = ident;
        this.apromore_edges = apromore_edges;
    }

    public int getIdent() {
        return ident;
    }

    public void setIdent(int ident) {
        this.ident = ident;
    }

    public apromore_CanonicalProcess getApromore_canonicalprocess() {
        return apromore_canonicalprocess;
    }

    public void setApromore_canonicalprocess(apromore_CanonicalProcess apromore_canonicalprocess) {
        this.apromore_canonicalprocess = apromore_canonicalprocess;
    }
    public apromore_CanonicalProcess getApromore_canonicalprocess() {
        return apromore_canonicalprocess;
    }

    public void setApromore_canonicalprocess(apromore_CanonicalProcess apromore_canonicalprocess) {
        this.apromore_canonicalprocess = apromore_canonicalprocess;
    }
    public apromore_Task getApromore_task() {
        return apromore_task;
    }

    public void setApromore_task(apromore_Task apromore_task) {
        this.apromore_task = apromore_task;
    }
    public List<apromore_Edge> getApromore_edges() {
        return apromore_edges;
    }

    public void addApromore_edge(Apromore_edge apromore_edge) {
        this.apromore_edges.add(apromore_edge);
    }

}