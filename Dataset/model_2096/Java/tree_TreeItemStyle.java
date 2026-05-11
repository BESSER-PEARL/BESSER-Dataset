





import java.util.List;
import java.util.ArrayList;

public class tree_TreeItemStyle extends Style, LabelStyle {

    private String backgroundColor;





    private tree_DTreeItem tree_dtreeitem;


    public tree_TreeItemStyle(
        String backgroundColor    ) {
        super(
        );
        this.backgroundColor = backgroundColor;
    }


    public String getBackgroundcolor() {
        return backgroundColor;
    }

    public void setBackgroundcolor(String backgroundColor) {
        this.backgroundColor = backgroundColor;
    }

    public tree_DTreeItem getTree_dtreeitem() {
        return tree_dtreeitem;
    }

    public void setTree_dtreeitem(tree_DTreeItem tree_dtreeitem) {
        this.tree_dtreeitem = tree_dtreeitem;
    }

}