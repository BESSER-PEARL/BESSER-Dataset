





import java.util.List;
import java.util.ArrayList;

public class uml_Node extends Class, DeploymentTarget {






    private List<uml_Node> uml_nodes;


    public uml_Node(
    ) {
        super(
        );
        this.uml_nodes = new ArrayList<>();
    }

    public uml_Node(
        ArrayList<uml_Node> uml_nodes    ) {
        this.uml_nodes = uml_nodes;
    }


    public List<uml_Node> getUml_nodes() {
        return uml_nodes;
    }

    public void addUml_node(Uml_node uml_node) {
        this.uml_nodes.add(uml_node);
    }

}