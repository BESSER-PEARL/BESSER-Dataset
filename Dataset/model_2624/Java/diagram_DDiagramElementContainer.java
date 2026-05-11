





import java.util.List;
import java.util.ArrayList;

public class diagram_DDiagramElementContainer extends AbstractDNode, DragAndDropTarget, EdgeTarget {

    private String width;
    private String height;





    private diagram_DDiagram diagram_ddiagram;




    private diagram_DDiagramElementContainer diagram_ddiagramelementcontainer;




    private List<diagram_DNode> diagram_dnodes;


    public diagram_DDiagramElementContainer(
        String width,        String height    ) {
        super(
        );
        this.width = width;
        this.height = height;
        this.diagram_dnodes = new ArrayList<>();
    }

    public diagram_DDiagramElementContainer(
        String width,        String height        ArrayList<diagram_DNode> diagram_dnodes    ) {
        this.width = width;
        this.height = height;
        this.diagram_dnodes = diagram_dnodes;
    }

    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }

    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }
    public diagram_DDiagramElementContainer getDiagram_ddiagramelementcontainer() {
        return diagram_ddiagramelementcontainer;
    }

    public void setDiagram_ddiagramelementcontainer(diagram_DDiagramElementContainer diagram_ddiagramelementcontainer) {
        this.diagram_ddiagramelementcontainer = diagram_ddiagramelementcontainer;
    }
    public List<diagram_DNode> getDiagram_dnodes() {
        return diagram_dnodes;
    }

    public void addDiagram_dnode(Diagram_dnode diagram_dnode) {
        this.diagram_dnodes.add(diagram_dnode);
    }

}