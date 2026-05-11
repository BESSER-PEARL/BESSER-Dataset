





import java.util.List;
import java.util.ArrayList;

public class viewers_TableViewerElement  {

    private String label;
    private String name;





    private viewers_TableViewerInput viewers_tableviewerinput;


    public viewers_TableViewerElement(
        String label,        String name    ) {
        this.label = label;
        this.name = name;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public viewers_TableViewerInput getViewers_tableviewerinput() {
        return viewers_tableviewerinput;
    }

    public void setViewers_tableviewerinput(viewers_TableViewerInput viewers_tableviewerinput) {
        this.viewers_tableviewerinput = viewers_tableviewerinput;
    }

}