





import java.util.List;
import java.util.ArrayList;

public class simpleGraph_Edge extends GraphElement {






    private List<simpleGraph_Nail> simplegraph_nails;




    private simpleGraph_Graph simplegraph_graph;




    private List<simpleGraph_Label> simplegraph_labels;


    public simpleGraph_Edge(
    ) {
        super(
        );
        this.simplegraph_nails = new ArrayList<>();
        this.simplegraph_labels = new ArrayList<>();
    }

    public simpleGraph_Edge(
        ArrayList<simpleGraph_Nail> simplegraph_nails,        ArrayList<simpleGraph_Label> simplegraph_labels    ) {
        this.simplegraph_nails = simplegraph_nails;
        this.simplegraph_labels = simplegraph_labels;
    }


    public List<simpleGraph_Nail> getSimplegraph_nails() {
        return simplegraph_nails;
    }

    public void addSimplegraph_nail(Simplegraph_nail simplegraph_nail) {
        this.simplegraph_nails.add(simplegraph_nail);
    }
    public simpleGraph_Graph getSimplegraph_graph() {
        return simplegraph_graph;
    }

    public void setSimplegraph_graph(simpleGraph_Graph simplegraph_graph) {
        this.simplegraph_graph = simplegraph_graph;
    }
    public List<simpleGraph_Label> getSimplegraph_labels() {
        return simplegraph_labels;
    }

    public void addSimplegraph_label(Simplegraph_label simplegraph_label) {
        this.simplegraph_labels.add(simplegraph_label);
    }

}