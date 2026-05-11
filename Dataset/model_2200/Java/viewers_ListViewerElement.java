





import java.util.List;
import java.util.ArrayList;

public class viewers_ListViewerElement  {

    private String label;





    private viewers_ListViewerInput viewers_listviewerinput;


    public viewers_ListViewerElement(
        String label    ) {
        this.label = label;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }

    public viewers_ListViewerInput getViewers_listviewerinput() {
        return viewers_listviewerinput;
    }

    public void setViewers_listviewerinput(viewers_ListViewerInput viewers_listviewerinput) {
        this.viewers_listviewerinput = viewers_listviewerinput;
    }

}