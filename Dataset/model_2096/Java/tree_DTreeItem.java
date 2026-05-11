





import java.util.List;
import java.util.ArrayList;

public class tree_DTreeItem extends DTreeItemContainer, DTreeElement {

    private boolean expanded;



    public tree_DTreeItem(
        boolean expanded    ) {
        super(
        );
        this.expanded = expanded;
    }


    public boolean getExpanded() {
        return expanded;
    }

    public void setExpanded(boolean expanded) {
        this.expanded = expanded;
    }


}