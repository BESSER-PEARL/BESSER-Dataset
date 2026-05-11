





import java.util.List;
import java.util.ArrayList;

public class sexec_ExecutionState extends ExecutionNode, ExecutionScope {

    private boolean leaf;



    public sexec_ExecutionState(
        boolean leaf    ) {
        super(
        );
        this.leaf = leaf;
    }


    public boolean getLeaf() {
        return leaf;
    }

    public void setLeaf(boolean leaf) {
        this.leaf = leaf;
    }


}