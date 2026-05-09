





import java.util.List;
import java.util.ArrayList;

public class model_diagram_MEDiagram extends Attachment {

    private String diagramLayout;
    private String type;



    public model_diagram_MEDiagram(
        String diagramLayout,        String type    ) {
        super(
        );
        this.diagramLayout = diagramLayout;
        this.type = type;
    }


    public String getDiagramlayout() {
        return diagramLayout;
    }

    public void setDiagramlayout(String diagramLayout) {
        this.diagramLayout = diagramLayout;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}