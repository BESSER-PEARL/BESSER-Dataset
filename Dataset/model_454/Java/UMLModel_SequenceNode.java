





import java.util.List;
import java.util.ArrayList;

public class UMLModel_SequenceNode extends StructuredActivityNode {






    private List<UMLModel_ExecutableNode> umlmodel_executablenodes;


    public UMLModel_SequenceNode(
    ) {
        super(
        );
        this.umlmodel_executablenodes = new ArrayList<>();
    }

    public UMLModel_SequenceNode(
        ArrayList<UMLModel_ExecutableNode> umlmodel_executablenodes    ) {
        this.umlmodel_executablenodes = umlmodel_executablenodes;
    }


    public List<UMLModel_ExecutableNode> getUmlmodel_executablenodes() {
        return umlmodel_executablenodes;
    }

    public void addUmlmodel_executablenode(Umlmodel_executablenode umlmodel_executablenode) {
        this.umlmodel_executablenodes.add(umlmodel_executablenode);
    }

}