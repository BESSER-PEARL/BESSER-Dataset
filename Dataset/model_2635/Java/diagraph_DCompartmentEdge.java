





import java.util.List;
import java.util.ArrayList;

public class diagraph_DCompartmentEdge extends DNestedEdge {

    private String partitionName;
    private int depth;



    public diagraph_DCompartmentEdge(
        String partitionName,        int depth    ) {
        super(
        );
        this.partitionName = partitionName;
        this.depth = depth;
    }


    public String getPartitionname() {
        return partitionName;
    }

    public void setPartitionname(String partitionName) {
        this.partitionName = partitionName;
    }
    public int getDepth() {
        return depth;
    }

    public void setDepth(int depth) {
        this.depth = depth;
    }


}