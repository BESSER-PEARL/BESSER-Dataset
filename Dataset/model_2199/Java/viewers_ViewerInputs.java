





import java.util.List;
import java.util.ArrayList;

public class viewers_ViewerInputs  {






    private List<viewers_TreeViewerInput> viewers_treeviewerinputs;


    public viewers_ViewerInputs(
    ) {
        this.viewers_treeviewerinputs = new ArrayList<>();
    }

    public viewers_ViewerInputs(
        ArrayList<viewers_TreeViewerInput> viewers_treeviewerinputs    ) {
        this.viewers_treeviewerinputs = viewers_treeviewerinputs;
    }


    public List<viewers_TreeViewerInput> getViewers_treeviewerinputs() {
        return viewers_treeviewerinputs;
    }

    public void addViewers_treeviewerinput(Viewers_treeviewerinput viewers_treeviewerinput) {
        this.viewers_treeviewerinputs.add(viewers_treeviewerinput);
    }

}