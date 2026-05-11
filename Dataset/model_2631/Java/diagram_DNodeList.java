





import java.util.List;
import java.util.ArrayList;

public class diagram_DNodeList extends DDiagramElementContainer {

    private int lineWidth;





    private List<diagram_DNodeListElement> diagram_dnodelistelements;


    public diagram_DNodeList(
        int lineWidth    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.diagram_dnodelistelements = new ArrayList<>();
    }

    public diagram_DNodeList(
        int lineWidth        ArrayList<diagram_DNodeListElement> diagram_dnodelistelements    ) {
        this.lineWidth = lineWidth;
        this.diagram_dnodelistelements = diagram_dnodelistelements;
    }

    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }

    public List<diagram_DNodeListElement> getDiagram_dnodelistelements() {
        return diagram_dnodelistelements;
    }

    public void addDiagram_dnodelistelement(Diagram_dnodelistelement diagram_dnodelistelement) {
        this.diagram_dnodelistelements.add(diagram_dnodelistelement);
    }

}