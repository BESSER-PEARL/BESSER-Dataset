





import java.util.List;
import java.util.ArrayList;

public class model_diagram_MEDiagram extends Attachment {

    private String type;
    private String diagramLayout;



    public model_diagram_MEDiagram(
        String type,        String diagramLayout    ) {
        super(
        );
        this.type = type;
        this.diagramLayout = diagramLayout;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDiagramlayout() {
        return diagramLayout;
    }

    public void setDiagramlayout(String diagramLayout) {
        this.diagramLayout = diagramLayout;
    }


}