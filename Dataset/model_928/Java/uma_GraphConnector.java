





import java.util.List;
import java.util.ArrayList;

public class uma_GraphConnector extends GraphElement {






    private uma_GraphEdge uma_graphedge;




    private List<uma_GraphEdge> uma_graphedges;


    public uma_GraphConnector(
    ) {
        super(
        );
        this.uma_graphedges = new ArrayList<>();
    }

    public uma_GraphConnector(
        ArrayList<uma_GraphEdge> uma_graphedges    ) {
        this.uma_graphedges = uma_graphedges;
    }


    public uma_GraphEdge getUma_graphedge() {
        return uma_graphedge;
    }

    public void setUma_graphedge(uma_GraphEdge uma_graphedge) {
        this.uma_graphedge = uma_graphedge;
    }
    public List<uma_GraphEdge> getUma_graphedges() {
        return uma_graphedges;
    }

    public void addUma_graphedge(Uma_graphedge uma_graphedge) {
        this.uma_graphedges.add(uma_graphedge);
    }

}