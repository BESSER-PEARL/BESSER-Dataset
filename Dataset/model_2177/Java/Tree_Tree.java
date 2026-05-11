





import java.util.List;
import java.util.ArrayList;

public class Tree_Tree  {

    private String label;





    private Tree_Tree tree_tree;




    private List<Tree_Tree> tree_trees;


    public Tree_Tree(
        String label    ) {
        this.label = label;
        this.tree_trees = new ArrayList<>();
    }

    public Tree_Tree(
        String label        ArrayList<Tree_Tree> tree_trees    ) {
        this.label = label;
        this.tree_trees = tree_trees;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public Tree_Tree getTree_tree() {
        return tree_tree;
    }

    public void setTree_tree(Tree_Tree tree_tree) {
        this.tree_tree = tree_tree;
    }
    public List<Tree_Tree> getTree_trees() {
        return tree_trees;
    }

    public void addTree_tree(Tree_tree tree_tree) {
        this.tree_trees.add(tree_tree);
    }

}