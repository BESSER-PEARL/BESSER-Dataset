





import java.util.List;
import java.util.ArrayList;

public class tree_Node  {

    private String label;
    private String data;





    private tree_Tree tree_tree;




    private List<tree_Node> tree_nodes;


    public tree_Node(
        String label,        String data    ) {
        this.label = label;
        this.data = data;
        this.tree_nodes = new ArrayList<>();
    }

    public tree_Node(
        String label,        String data        ArrayList<tree_Node> tree_nodes    ) {
        this.label = label;
        this.data = data;
        this.tree_nodes = tree_nodes;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }

    public tree_Tree getTree_tree() {
        return tree_tree;
    }

    public void setTree_tree(tree_Tree tree_tree) {
        this.tree_tree = tree_tree;
    }
    public List<tree_Node> getTree_nodes() {
        return tree_nodes;
    }

    public void addTree_node(Tree_node tree_node) {
        this.tree_nodes.add(tree_node);
    }

}