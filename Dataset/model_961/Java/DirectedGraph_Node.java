





import java.util.List;
import java.util.ArrayList;

public class DirectedGraph_Node extends GraphElement {

    private String label;



    public DirectedGraph_Node(
        String label    ) {
        super(
        );
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }


}