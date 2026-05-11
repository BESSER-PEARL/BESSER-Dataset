





import java.util.List;
import java.util.ArrayList;

public class tree_Node  {

    private String name;





    private tree_Tree tree_tree;




    private tree_Node tree_node;


    public tree_Node(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tree_Tree getTree_tree() {
        return tree_tree;
    }

    public void setTree_tree(tree_Tree tree_tree) {
        this.tree_tree = tree_tree;
    }
    public tree_Node getTree_node() {
        return tree_node;
    }

    public void setTree_node(tree_Node tree_node) {
        this.tree_node = tree_node;
    }

}