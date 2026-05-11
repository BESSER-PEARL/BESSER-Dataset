





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DNodeList extends DDiagramElementContainer {

    private int lineWidth;





    private List<DNodeListElement> dnodelistelements;


    public viewpoint_diagram_DNodeList(
        int lineWidth    ) {
        super(
        );
        this.lineWidth = lineWidth;
        this.dnodelistelements = new ArrayList<>();
    }

    public viewpoint_diagram_DNodeList(
        int lineWidth        ArrayList<DNodeListElement> dnodelistelements    ) {
        this.lineWidth = lineWidth;
        this.dnodelistelements = dnodelistelements;
    }

    public int getLinewidth() {
        return lineWidth;
    }

    public void setLinewidth(int lineWidth) {
        this.lineWidth = lineWidth;
    }

    public List<DNodeListElement> getDnodelistelements() {
        return dnodelistelements;
    }

    public void addDnodelistelement(Dnodelistelement dnodelistelement) {
        this.dnodelistelements.add(dnodelistelement);
    }

}