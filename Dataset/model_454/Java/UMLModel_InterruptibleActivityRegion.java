





import java.util.List;
import java.util.ArrayList;

public class UMLModel_InterruptibleActivityRegion extends ActivityGroup {

    private String interruptingEdge;
    private String node;



    public UMLModel_InterruptibleActivityRegion(
        String interruptingEdge,        String node    ) {
        super(
        );
        this.interruptingEdge = interruptingEdge;
        this.node = node;
    }


    public String getInterruptingedge() {
        return interruptingEdge;
    }

    public void setInterruptingedge(String interruptingEdge) {
        this.interruptingEdge = interruptingEdge;
    }
    public String getNode() {
        return node;
    }

    public void setNode(String node) {
        this.node = node;
    }


}