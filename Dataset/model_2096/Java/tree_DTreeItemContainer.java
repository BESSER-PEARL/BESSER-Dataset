





import java.util.List;
import java.util.ArrayList;

public class tree_DTreeItemContainer extends DSemanticDecorator {






    private tree_DTreeItem tree_dtreeitem;




    private List<tree_DTreeItem> tree_dtreeitems;


    public tree_DTreeItemContainer(
    ) {
        super(
        );
        this.tree_dtreeitems = new ArrayList<>();
    }

    public tree_DTreeItemContainer(
        ArrayList<tree_DTreeItem> tree_dtreeitems    ) {
        this.tree_dtreeitems = tree_dtreeitems;
    }


    public tree_DTreeItem getTree_dtreeitem() {
        return tree_dtreeitem;
    }

    public void setTree_dtreeitem(tree_DTreeItem tree_dtreeitem) {
        this.tree_dtreeitem = tree_dtreeitem;
    }
    public List<tree_DTreeItem> getTree_dtreeitems() {
        return tree_dtreeitems;
    }

    public void addTree_dtreeitem(Tree_dtreeitem tree_dtreeitem) {
        this.tree_dtreeitems.add(tree_dtreeitem);
    }

}