





import java.util.List;
import java.util.ArrayList;

public class model_diagram_MEDiagram extends Attachment {

    private String type;
    private String diagramLayout;





    private diagram_model_Diagram diagram_model_diagram;




    private List<UnicaseModelElement> unicasemodelelements;




    private List<UnicaseModelElement> unicasemodelelements;


    public model_diagram_MEDiagram(
        String type,        String diagramLayout    ) {
        super(
        );
        this.type = type;
        this.diagramLayout = diagramLayout;
        this.unicasemodelelements = new ArrayList<>();
        this.unicasemodelelements = new ArrayList<>();
    }

    public model_diagram_MEDiagram(
        String type,        String diagramLayout        ArrayList<UnicaseModelElement> unicasemodelelements,        ArrayList<UnicaseModelElement> unicasemodelelements    ) {
        this.type = type;
        this.diagramLayout = diagramLayout;
        this.unicasemodelelements = unicasemodelelements;
        this.unicasemodelelements = unicasemodelelements;
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

    public diagram_model_Diagram getDiagram_model_diagram() {
        return diagram_model_diagram;
    }

    public void setDiagram_model_diagram(diagram_model_Diagram diagram_model_diagram) {
        this.diagram_model_diagram = diagram_model_diagram;
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