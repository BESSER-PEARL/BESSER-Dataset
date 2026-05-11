





import java.util.List;
import java.util.ArrayList;

public class OverlappingTree_NodeKind  {






    private OverlappingTree_Tree overlappingtree_tree;




    private List<OverlappingTree_Tree> overlappingtree_trees;


    public OverlappingTree_NodeKind(
    ) {
        this.overlappingtree_trees = new ArrayList<>();
    }

    public OverlappingTree_NodeKind(
        ArrayList<OverlappingTree_Tree> overlappingtree_trees    ) {
        this.overlappingtree_trees = overlappingtree_trees;
    }


    public OverlappingTree_Tree getOverlappingtree_tree() {
        return overlappingtree_tree;
    }

    public void setOverlappingtree_tree(OverlappingTree_Tree overlappingtree_tree) {
        this.overlappingtree_tree = overlappingtree_tree;
    }
    public List<OverlappingTree_Tree> getOverlappingtree_trees() {
        return overlappingtree_trees;
    }

    public void addOverlappingtree_tree(Overlappingtree_tree overlappingtree_tree) {
        this.overlappingtree_trees.add(overlappingtree_tree);
    }

}