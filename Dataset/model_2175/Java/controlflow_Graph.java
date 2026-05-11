





import java.util.List;
import java.util.ArrayList;

public class controlflow_Graph  {






    private List<controlflow_Node> controlflow_nodes;




    private controlflow_Node controlflow_node;


    public controlflow_Graph(
    ) {
        this.controlflow_nodes = new ArrayList<>();
    }

    public controlflow_Graph(
        ArrayList<controlflow_Node> controlflow_nodes    ) {
        this.controlflow_nodes = controlflow_nodes;
    }


    public List<controlflow_Node> getControlflow_nodes() {
        return controlflow_nodes;
    }

    public void addControlflow_node(Controlflow_node controlflow_node) {
        this.controlflow_nodes.add(controlflow_node);
    }
    public controlflow_Node getControlflow_node() {
        return controlflow_node;
    }

    public void setControlflow_node(controlflow_Node controlflow_node) {
        this.controlflow_node = controlflow_node;
    }

}