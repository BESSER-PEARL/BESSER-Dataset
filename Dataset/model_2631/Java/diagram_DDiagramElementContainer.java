





import java.util.List;
import java.util.ArrayList;

public class diagram_DDiagramElementContainer extends AbstractDNode, DContainer, EdgeTarget, DragAndDropTarget {

    private String width;
    private String height;





    private List<diagram_DDiagramElementContainer> diagram_ddiagramelementcontainers;




    private diagram_DDiagram diagram_ddiagram;


    public diagram_DDiagramElementContainer(
        String width,        String height    ) {
        super(
        );
        this.width = width;
        this.height = height;
        this.diagram_ddiagramelementcontainers = new ArrayList<>();
    }

    public diagram_DDiagramElementContainer(
        String width,        String height        ArrayList<diagram_DDiagramElementContainer> diagram_ddiagramelementcontainers    ) {
        this.width = width;
        this.height = height;
        this.diagram_ddiagramelementcontainers = diagram_ddiagramelementcontainers;
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

    public List<diagram_DDiagramElementContainer> getDiagram_ddiagramelementcontainers() {
        return diagram_ddiagramelementcontainers;
    }

    public void addDiagram_ddiagramelementcontainer(Diagram_ddiagramelementcontainer diagram_ddiagramelementcontainer) {
        this.diagram_ddiagramelementcontainers.add(diagram_ddiagramelementcontainer);
    }
    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }

}