





import java.util.List;
import java.util.ArrayList;

public class uml_SequenceNode extends StructuredActivityNode {






    private List<uml_ExecutableNode> uml_executablenodes;


    public uml_SequenceNode(
    ) {
        super(
        );
        this.uml_executablenodes = new ArrayList<>();
    }

    public uml_SequenceNode(
        ArrayList<uml_ExecutableNode> uml_executablenodes    ) {
        this.uml_executablenodes = uml_executablenodes;
    }


    public List<uml_ExecutableNode> getUml_executablenodes() {
        return uml_executablenodes;
    }

    public void addUml_executablenode(Uml_executablenode uml_executablenode) {
        this.uml_executablenodes.add(uml_executablenode);
    }

}