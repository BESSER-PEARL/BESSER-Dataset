





import java.util.List;
import java.util.ArrayList;

public class UML2_Node extends Class, DeploymentTarget {






    private List<UML2_Node> uml2_nodes;


    public UML2_Node(
    ) {
        super(
        );
        this.uml2_nodes = new ArrayList<>();
    }

    public UML2_Node(
        ArrayList<UML2_Node> uml2_nodes    ) {
        this.uml2_nodes = uml2_nodes;
    }


    public List<UML2_Node> getUml2_nodes() {
        return uml2_nodes;
    }

    public void addUml2_node(Uml2_node uml2_node) {
        this.uml2_nodes.add(uml2_node);
    }

}