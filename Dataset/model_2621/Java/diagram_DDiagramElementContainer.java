





import java.util.List;
import java.util.ArrayList;

public class diagram_DDiagramElementContainer extends DragAndDropTarget, AbstractDNode, EdgeTarget {

    private String height;
    private String width;





    private diagram_DDiagram diagram_ddiagram;




    private diagram_DDiagramElementContainer diagram_ddiagramelementcontainer;


    public diagram_DDiagramElementContainer(
        String height,        String width    ) {
        super(
        );
        this.height = height;
        this.width = width;
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
    public diagram_DDiagramElementContainer getDiagram_ddiagramelementcontainer() {
        return diagram_ddiagramelementcontainer;
    }

    public void setDiagram_ddiagramelementcontainer(diagram_DDiagramElementContainer diagram_ddiagramelementcontainer) {
        this.diagram_ddiagramelementcontainer = diagram_ddiagramelementcontainer;
    }

}