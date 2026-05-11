





import java.util.List;
import java.util.ArrayList;

public class ed2_Node extends TreeElement {






    private List<ed2_Node> ed2_nodes;


    public ed2_Node(
    ) {
        super(
        );
        this.ed2_nodes = new ArrayList<>();
    }

    public ed2_Node(
        ArrayList<ed2_Node> ed2_nodes    ) {
        this.ed2_nodes = ed2_nodes;
    }


    public List<ed2_Node> getEd2_nodes() {
        return ed2_nodes;
    }

    public void addEd2_node(Ed2_node ed2_node) {
        this.ed2_nodes.add(ed2_node);
    }

}