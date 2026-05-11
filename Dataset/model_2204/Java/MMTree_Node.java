





import java.util.List;
import java.util.ArrayList;

public class MMTree_Node extends TreeElement {






    private List<MMTree_TreeElement> mmtree_treeelements;


    public MMTree_Node(
    ) {
        super(
        );
        this.mmtree_treeelements = new ArrayList<>();
    }

    public MMTree_Node(
        ArrayList<MMTree_TreeElement> mmtree_treeelements    ) {
        this.mmtree_treeelements = mmtree_treeelements;
    }


    public List<MMTree_TreeElement> getMmtree_treeelements() {
        return mmtree_treeelements;
    }

    public void addMmtree_treeelement(Mmtree_treeelement mmtree_treeelement) {
        this.mmtree_treeelements.add(mmtree_treeelement);
    }

}