





import java.util.List;
import java.util.ArrayList;

public class TreeDsl_Tree  {

    private String label;





    private List<TreeDsl_Tree> treedsl_trees;




    private TreeDsl_Tree treedsl_tree;


    public TreeDsl_Tree(
        String label    ) {
        this.label = label;
        this.treedsl_trees = new ArrayList<>();
    }

    public TreeDsl_Tree(
        String label        ArrayList<TreeDsl_Tree> treedsl_trees    ) {
        this.label = label;
        this.treedsl_trees = treedsl_trees;
    }

    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public List<TreeDsl_Tree> getTreedsl_trees() {
        return treedsl_trees;
    }

    public void addTreedsl_tree(Treedsl_tree treedsl_tree) {
        this.treedsl_trees.add(treedsl_tree);
    }
    public TreeDsl_Tree getTreedsl_tree() {
        return treedsl_tree;
    }

    public void setTreedsl_tree(TreeDsl_Tree treedsl_tree) {
        this.treedsl_tree = treedsl_tree;
    }

}