





import java.util.List;
import java.util.ArrayList;

public class vml_Graph extends Diagram {

    private String title;
    private String ID;





    private vml_GraphStyle vml_graphstyle;


    public vml_Graph(
        String title,        String ID    ) {
        super(
        );
        this.title = title;
        this.ID = ID;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }

    public vml_GraphStyle getVml_graphstyle() {
        return vml_graphstyle;
    }

    public void setVml_graphstyle(vml_GraphStyle vml_graphstyle) {
        this.vml_graphstyle = vml_graphstyle;
    }

}