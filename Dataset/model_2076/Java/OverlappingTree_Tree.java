





import java.util.List;
import java.util.ArrayList;

public class OverlappingTree_Tree  {






    private List<OverlappingTree_Child> overlappingtree_childs;


    public OverlappingTree_Tree(
    ) {
        this.overlappingtree_childs = new ArrayList<>();
    }

    public OverlappingTree_Tree(
        ArrayList<OverlappingTree_Child> overlappingtree_childs    ) {
        this.overlappingtree_childs = overlappingtree_childs;
    }


    public List<OverlappingTree_Child> getOverlappingtree_childs() {
        return overlappingtree_childs;
    }

    public void addOverlappingtree_child(Overlappingtree_child overlappingtree_child) {
        this.overlappingtree_childs.add(overlappingtree_child);
    }

}