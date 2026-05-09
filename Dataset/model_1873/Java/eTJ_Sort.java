





import java.util.List;
import java.util.ArrayList;

public class eTJ_Sort extends SortResources, SortAccounts, SortTasks, SortJournalEntries {

    private boolean tree;



    public eTJ_Sort(
        boolean tree    ) {
        super(
        );
        this.tree = tree;
    }


    public boolean getTree() {
        return tree;
    }

    public void setTree(boolean tree) {
        this.tree = tree;
    }


}