





import java.util.List;
import java.util.ArrayList;

public class tree_Node  {

    private String name;





    private tree_Node tree_node;




    private List<tree_Node> tree_nodes;


    public tree_Node(
        String name    ) {
        this.name = name;
        this.tree_nodes = new ArrayList<>();
    }

    public tree_Node(
        String name        ArrayList<tree_Node> tree_nodes    ) {
        this.name = name;
        this.tree_nodes = tree_nodes;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tree_Node getTree_node() {
        return tree_node;
    }

    public void setTree_node(tree_Node tree_node) {
        this.tree_node = tree_node;
    }
    public List<tree_Node> getTree_nodes() {
        return tree_nodes;
    }

    public void addTree_node(Tree_node tree_node) {
        this.tree_nodes.add(tree_node);
    }

}