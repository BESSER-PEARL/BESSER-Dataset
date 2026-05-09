





import java.util.List;
import java.util.ArrayList;

public class transformr_Node extends GraphElement {






    private List<transformr_Edge> transformr_edges;




    private transformr_Edge transformr_edge;




    private List<transformr_Attribute> transformr_attributes;




    private transformr_Graph transformr_graph;


    public transformr_Node(
    ) {
        super(
        );
        this.transformr_edges = new ArrayList<>();
        this.transformr_attributes = new ArrayList<>();
    }

    public transformr_Node(
        ArrayList<transformr_Edge> transformr_edges,        ArrayList<transformr_Attribute> transformr_attributes    ) {
        this.transformr_edges = transformr_edges;
        this.transformr_attributes = transformr_attributes;
    }


    public List<transformr_Edge> getTransformr_edges() {
        return transformr_edges;
    }

    public void addTransformr_edge(Transformr_edge transformr_edge) {
        this.transformr_edges.add(transformr_edge);
    }
    public transformr_Edge getTransformr_edge() {
        return transformr_edge;
    }

    public void setTransformr_edge(transformr_Edge transformr_edge) {
        this.transformr_edge = transformr_edge;
    }
    public List<transformr_Attribute> getTransformr_attributes() {
        return transformr_attributes;
    }

    public void addTransformr_attribute(Transformr_attribute transformr_attribute) {
        this.transformr_attributes.add(transformr_attribute);
    }
    public transformr_Graph getTransformr_graph() {
        return transformr_graph;
    }

    public void setTransformr_graph(transformr_Graph transformr_graph) {
        this.transformr_graph = transformr_graph;
    }

}