





import java.util.List;
import java.util.ArrayList;

public class Tree_Node  {

    private int value;





    private List<Tree_Node> tree_nodes;


    public Tree_Node(
        int value    ) {
        this.value = value;
        this.tree_nodes = new ArrayList<>();
    }

    public Tree_Node(
        int value        ArrayList<Tree_Node> tree_nodes    ) {
        this.value = value;
        this.tree_nodes = tree_nodes;
    }

    public int getValue() {
        return value;
    }

    public void setValue(int value) {
        this.value = value;
    }

    public List<Tree_Node> getTree_nodes() {
        return tree_nodes;
    }

    public void addTree_node(Tree_node tree_node) {
        this.tree_nodes.add(tree_node);
    }

}