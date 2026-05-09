





import java.util.List;
import java.util.ArrayList;

public class transformr_Node extends GraphElement {






    private List<transformr_Attribute> transformr_attributes;




    private transformr_Graph transformr_graph;


    public transformr_Node(
    ) {
        super(
        );
        this.transformr_attributes = new ArrayList<>();
    }

    public transformr_Node(
        ArrayList<transformr_Attribute> transformr_attributes    ) {
        this.transformr_attributes = transformr_attributes;
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