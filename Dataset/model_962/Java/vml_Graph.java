





import java.util.List;
import java.util.ArrayList;

public class vml_Graph  {

    private String title;
    private String ID;





    private vml_Diagram vml_diagram;


    public vml_Graph(
        String title,        String ID    ) {
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

    public vml_Diagram getVml_diagram() {
        return vml_diagram;
    }

    public void setVml_diagram(vml_Diagram vml_diagram) {
        this.vml_diagram = vml_diagram;
    }

}