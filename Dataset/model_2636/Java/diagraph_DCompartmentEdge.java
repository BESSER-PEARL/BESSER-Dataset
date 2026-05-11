





import java.util.List;
import java.util.ArrayList;

public class diagraph_DCompartmentEdge extends DNestedEdge {

    private int depth;
    private String partitionName;



    public diagraph_DCompartmentEdge(
        int depth,        String partitionName    ) {
        super(
        );
        this.depth = depth;
        this.partitionName = partitionName;
    }


    public int getDepth() {
        return depth;
    }

    public void setDepth(int depth) {
        this.depth = depth;
    }
    public String getPartitionname() {
        return partitionName;
    }

    public void setPartitionname(String partitionName) {
        this.partitionName = partitionName;
    }


}