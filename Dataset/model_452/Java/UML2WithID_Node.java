





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Node extends Class, DeploymentTarget {






    private List<UML2WithID_Node> uml2withid_nodes;


    public UML2WithID_Node(
    ) {
        super(
        );
        this.uml2withid_nodes = new ArrayList<>();
    }

    public UML2WithID_Node(
        ArrayList<UML2WithID_Node> uml2withid_nodes    ) {
        this.uml2withid_nodes = uml2withid_nodes;
    }


    public List<UML2WithID_Node> getUml2withid_nodes() {
        return uml2withid_nodes;
    }

    public void addUml2withid_node(Uml2withid_node uml2withid_node) {
        this.uml2withid_nodes.add(uml2withid_node);
    }

}