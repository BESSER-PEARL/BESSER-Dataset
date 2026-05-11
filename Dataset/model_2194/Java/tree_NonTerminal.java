





import java.util.List;
import java.util.ArrayList;

public class tree_NonTerminal extends TreeNode {






    private List<tree_TreeNode> tree_treenodes;


    public tree_NonTerminal(
    ) {
        super(
        );
        this.tree_treenodes = new ArrayList<>();
    }

    public tree_NonTerminal(
        ArrayList<tree_TreeNode> tree_treenodes    ) {
        this.tree_treenodes = tree_treenodes;
    }


    public List<tree_TreeNode> getTree_treenodes() {
        return tree_treenodes;
    }

    public void addTree_treenode(Tree_treenode tree_treenode) {
        this.tree_treenodes.add(tree_treenode);
    }

}