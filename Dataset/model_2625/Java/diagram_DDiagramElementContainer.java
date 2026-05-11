





import java.util.List;
import java.util.ArrayList;

public class diagram_DDiagramElementContainer extends EdgeTarget, AbstractDNode, DragAndDropTarget {

    private String height;
    private String width;





    private diagram_DDiagram diagram_ddiagram;




    private List<diagram_DDiagramElement> diagram_ddiagramelements;




    private List<diagram_DDiagramElementContainer> diagram_ddiagramelementcontainers;




    private List<diagram_DNode> diagram_dnodes;


    public diagram_DDiagramElementContainer(
        String height,        String width    ) {
        super(
        );
        this.height = height;
        this.width = width;
        this.diagram_ddiagramelements = new ArrayList<>();
        this.diagram_ddiagramelementcontainers = new ArrayList<>();
        this.diagram_dnodes = new ArrayList<>();
    }

    public diagram_DDiagramElementContainer(
        String height,        String width        ArrayList<diagram_DDiagramElement> diagram_ddiagramelements,        ArrayList<diagram_DDiagramElementContainer> diagram_ddiagramelementcontainers,        ArrayList<diagram_DNode> diagram_dnodes    ) {
        this.height = height;
        this.width = width;
        this.diagram_ddiagramelements = diagram_ddiagramelements;
        this.diagram_ddiagramelementcontainers = diagram_ddiagramelementcontainers;
        this.diagram_dnodes = diagram_dnodes;
    }

    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }

    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }
    public List<diagram_DDiagramElement> getDiagram_ddiagramelements() {
        return diagram_ddiagramelements;
    }

    public void addDiagram_ddiagramelement(Diagram_ddiagramelement diagram_ddiagramelement) {
        this.diagram_ddiagramelements.add(diagram_ddiagramelement);
    }
    public List<diagram_DDiagramElementContainer> getDiagram_ddiagramelementcontainers() {
        return diagram_ddiagramelementcontainers;
    }

    public void addDiagram_ddiagramelementcontainer(Diagram_ddiagramelementcontainer diagram_ddiagramelementcontainer) {
        this.diagram_ddiagramelementcontainers.add(diagram_ddiagramelementcontainer);
    }
    public List<diagram_DNode> getDiagram_dnodes() {
        return diagram_dnodes;
    }

    public void addDiagram_dnode(Diagram_dnode diagram_dnode) {
        this.diagram_dnodes.add(diagram_dnode);
    }

}