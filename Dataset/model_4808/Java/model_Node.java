





import java.util.List;
import java.util.ArrayList;

public class model_Node  {

    private String label;





    private model_Node model_node;




    private model_Node model_node;




    private model_Node model_node;




    private List<model_Node> model_nodes;




    private model_Node model_node;


    public model_Node(
        String label    ) {
        this.label = label;
        this.model_nodes = new ArrayList<>();
    }

    public model_Node(
        String label        ArrayList<model_Node> model_nodes    ) {
        this.label = label;
        this.model_nodes = model_nodes;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public model_Node getModel_node() {
        return model_node;
    }

    public void setModel_node(model_Node model_node) {
        this.model_node = model_node;
    }
    public model_Node getModel_node() {
        return model_node;
    }

    public void setModel_node(model_Node model_node) {
        this.model_node = model_node;
    }
    public model_Node getModel_node() {
        return model_node;
    }

    public void setModel_node(model_Node model_node) {
        this.model_node = model_node;
    }
    public List<model_Node> getModel_nodes() {
        return model_nodes;
    }

    public void addModel_node(Model_node model_node) {
        this.model_nodes.add(model_node);
    }
    public model_Node getModel_node() {
        return model_node;
    }

    public void setModel_node(model_Node model_node) {
        this.model_node = model_node;
    }

}