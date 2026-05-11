





import java.util.List;
import java.util.ArrayList;

public class Tree_Storage  {






    private List<Tree_Node> tree_nodes;


    public Tree_Storage(
    ) {
        this.tree_nodes = new ArrayList<>();
    }

    public Tree_Storage(
        ArrayList<Tree_Node> tree_nodes    ) {
        this.tree_nodes = tree_nodes;
    }


    public List<Tree_Node> getTree_nodes() {
        return tree_nodes;
    }

    public void addTree_node(Tree_node tree_node) {
        this.tree_nodes.add(tree_node);
    }

}