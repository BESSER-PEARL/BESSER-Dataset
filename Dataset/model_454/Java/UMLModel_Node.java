





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Node extends DeploymentTarget, Class {






    private List<UMLModel_Node> umlmodel_nodes;


    public UMLModel_Node(
    ) {
        super(
        );
        this.umlmodel_nodes = new ArrayList<>();
    }

    public UMLModel_Node(
        ArrayList<UMLModel_Node> umlmodel_nodes    ) {
        this.umlmodel_nodes = umlmodel_nodes;
    }


    public List<UMLModel_Node> getUmlmodel_nodes() {
        return umlmodel_nodes;
    }

    public void addUmlmodel_node(Umlmodel_node umlmodel_node) {
        this.umlmodel_nodes.add(umlmodel_node);
    }

}