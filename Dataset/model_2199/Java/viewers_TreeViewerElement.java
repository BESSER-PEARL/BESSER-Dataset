





import java.util.List;
import java.util.ArrayList;

public class viewers_TreeViewerElement  {

    private String label;





    private viewers_TreeViewerInput viewers_treeviewerinput;




    private viewers_TreeViewerElement viewers_treeviewerelement;


    public viewers_TreeViewerElement(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public viewers_TreeViewerInput getViewers_treeviewerinput() {
        return viewers_treeviewerinput;
    }

    public void setViewers_treeviewerinput(viewers_TreeViewerInput viewers_treeviewerinput) {
        this.viewers_treeviewerinput = viewers_treeviewerinput;
    }
    public viewers_TreeViewerElement getViewers_treeviewerelement() {
        return viewers_treeviewerelement;
    }

    public void setViewers_treeviewerelement(viewers_TreeViewerElement viewers_treeviewerelement) {
        this.viewers_treeviewerelement = viewers_treeviewerelement;
    }

}