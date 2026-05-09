





import java.util.List;
import java.util.ArrayList;

public class model_diagram_MEDiagram extends Attachment {

    private String diagramLayout;
    private String type;





    private List<UnicaseModelElement> unicasemodelelements;




    private List<UnicaseModelElement> unicasemodelelements;


    public model_diagram_MEDiagram(
        String diagramLayout,        String type    ) {
        super(
        );
        this.diagramLayout = diagramLayout;
        this.type = type;
        this.unicasemodelelements = new ArrayList<>();
        this.unicasemodelelements = new ArrayList<>();
    }

    public model_diagram_MEDiagram(
        String diagramLayout,        String type        ArrayList<UnicaseModelElement> unicasemodelelements,        ArrayList<UnicaseModelElement> unicasemodelelements    ) {
        this.diagramLayout = diagramLayout;
        this.type = type;
        this.unicasemodelelements = unicasemodelelements;
        this.unicasemodelelements = unicasemodelelements;
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

    public List<UnicaseModelElement> getUnicasemodelelements() {
        return unicasemodelelements;
    }

    public void addUnicasemodelelement(Unicasemodelelement unicasemodelelement) {
        this.unicasemodelelements.add(unicasemodelelement);
    }
    public List<UnicaseModelElement> getUnicasemodelelements() {
        return unicasemodelelements;
    }

    public void addUnicasemodelelement(Unicasemodelelement unicasemodelelement) {
        this.unicasemodelelements.add(unicasemodelelement);
    }

}