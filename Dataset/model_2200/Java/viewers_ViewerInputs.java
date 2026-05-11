





import java.util.List;
import java.util.ArrayList;

public class viewers_ViewerInputs  {






    private List<viewers_TreeViewerInput> viewers_treeviewerinputs;




    private List<viewers_TableViewerInput> viewers_tableviewerinputs;




    private List<viewers_ListViewerInput> viewers_listviewerinputs;


    public viewers_ViewerInputs(
    ) {
        this.viewers_treeviewerinputs = new ArrayList<>();
        this.viewers_tableviewerinputs = new ArrayList<>();
        this.viewers_listviewerinputs = new ArrayList<>();
    }

    public viewers_ViewerInputs(
        ArrayList<viewers_TreeViewerInput> viewers_treeviewerinputs,        ArrayList<viewers_TableViewerInput> viewers_tableviewerinputs,        ArrayList<viewers_ListViewerInput> viewers_listviewerinputs    ) {
        this.viewers_treeviewerinputs = viewers_treeviewerinputs;
        this.viewers_tableviewerinputs = viewers_tableviewerinputs;
        this.viewers_listviewerinputs = viewers_listviewerinputs;
    }


    public List<viewers_TreeViewerInput> getViewers_treeviewerinputs() {
        return viewers_treeviewerinputs;
    }

    public void addViewers_treeviewerinput(Viewers_treeviewerinput viewers_treeviewerinput) {
        this.viewers_treeviewerinputs.add(viewers_treeviewerinput);
    }
    public List<viewers_TableViewerInput> getViewers_tableviewerinputs() {
        return viewers_tableviewerinputs;
    }

    public void addViewers_tableviewerinput(Viewers_tableviewerinput viewers_tableviewerinput) {
        this.viewers_tableviewerinputs.add(viewers_tableviewerinput);
    }
    public List<viewers_ListViewerInput> getViewers_listviewerinputs() {
        return viewers_listviewerinputs;
    }

    public void addViewers_listviewerinput(Viewers_listviewerinput viewers_listviewerinput) {
        this.viewers_listviewerinputs.add(viewers_listviewerinput);
    }

}