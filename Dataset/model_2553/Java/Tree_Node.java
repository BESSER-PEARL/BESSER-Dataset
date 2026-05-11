





import java.util.List;
import java.util.ArrayList;

public class Tree_Node  {

    private String id;





    private List<Tree_Node> tree_nodes;




    private Tree_Node tree_node;


    public Tree_Node(
        String id    ) {
        this.id = id;
        this.tree_nodes = new ArrayList<>();
    }

    public Tree_Node(
        String id        ArrayList<Tree_Node> tree_nodes    ) {
        this.id = id;
        this.tree_nodes = tree_nodes;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<Tree_Node> getTree_nodes() {
        return tree_nodes;
    }

    public void addTree_node(Tree_node tree_node) {
        this.tree_nodes.add(tree_node);
    }
    public Tree_Node getTree_node() {
        return tree_node;
    }

    public void setTree_node(Tree_Node tree_node) {
        this.tree_node = tree_node;
    }

}