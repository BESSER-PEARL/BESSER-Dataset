





import java.util.List;
import java.util.ArrayList;

public class digraph_Node extends GraphElement {

    private String label;



    public digraph_Node(
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