





import java.util.List;
import java.util.ArrayList;

public class project_Sort extends SortJournalEntries, SortTasks, SortAccounts, SortResources {

    private boolean tree;



    public project_Sort(
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