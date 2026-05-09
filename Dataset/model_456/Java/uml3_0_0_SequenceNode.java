





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_SequenceNode extends StructuredActivityNode {






    private List<uml3_0_0_ExecutableNode> uml3_0_0_executablenodes;


    public uml3_0_0_SequenceNode(
    ) {
        super(
        );
        this.uml3_0_0_executablenodes = new ArrayList<>();
    }

    public uml3_0_0_SequenceNode(
        ArrayList<uml3_0_0_ExecutableNode> uml3_0_0_executablenodes    ) {
        this.uml3_0_0_executablenodes = uml3_0_0_executablenodes;
    }


    public List<uml3_0_0_ExecutableNode> getUml3_0_0_executablenodes() {
        return uml3_0_0_executablenodes;
    }

    public void addUml3_0_0_executablenode(Uml3_0_0_executablenode uml3_0_0_executablenode) {
        this.uml3_0_0_executablenodes.add(uml3_0_0_executablenode);
    }

}