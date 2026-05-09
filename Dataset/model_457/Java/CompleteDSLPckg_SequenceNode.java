





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_SequenceNode extends StructuredActivityNode {






    private List<CompleteDSLPckg_ExecutableNode> completedslpckg_executablenodes;


    public CompleteDSLPckg_SequenceNode(
    ) {
        super(
        );
        this.completedslpckg_executablenodes = new ArrayList<>();
    }

    public CompleteDSLPckg_SequenceNode(
        ArrayList<CompleteDSLPckg_ExecutableNode> completedslpckg_executablenodes    ) {
        this.completedslpckg_executablenodes = completedslpckg_executablenodes;
    }


    public List<CompleteDSLPckg_ExecutableNode> getCompletedslpckg_executablenodes() {
        return completedslpckg_executablenodes;
    }

    public void addCompletedslpckg_executablenode(Completedslpckg_executablenode completedslpckg_executablenode) {
        this.completedslpckg_executablenodes.add(completedslpckg_executablenode);
    }

}