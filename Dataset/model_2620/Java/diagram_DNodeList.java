





import java.util.List;
import java.util.ArrayList;

public class diagram_DNodeList extends DDiagramElementContainer {






    private List<diagram_DNodeListElement> diagram_dnodelistelements;


    public diagram_DNodeList(
    ) {
        super(
        );
        this.diagram_dnodelistelements = new ArrayList<>();
    }

    public diagram_DNodeList(
        ArrayList<diagram_DNodeListElement> diagram_dnodelistelements    ) {
        this.diagram_dnodelistelements = diagram_dnodelistelements;
    }


    public List<diagram_DNodeListElement> getDiagram_dnodelistelements() {
        return diagram_dnodelistelements;
    }

    public void addDiagram_dnodelistelement(Diagram_dnodelistelement diagram_dnodelistelement) {
        this.diagram_dnodelistelements.add(diagram_dnodelistelement);
    }

}