





import java.util.List;
import java.util.ArrayList;

public class diagram_DNode extends AbstractDNode, EdgeTarget, DragAndDropTarget {

    private String labelPosition;
    private String resizeKind;
    private String height;
    private String width;





    private diagram_DDiagramElementContainer diagram_ddiagramelementcontainer;




    private diagram_DDiagram diagram_ddiagram;


    public diagram_DNode(
        String labelPosition,        String resizeKind,        String height,        String width    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.resizeKind = resizeKind;
        this.height = height;
        this.width = width;
    }


    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public String getResizekind() {
        return resizeKind;
    }

    public void setResizekind(String resizeKind) {
        this.resizeKind = resizeKind;
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

    public diagram_DDiagramElementContainer getDiagram_ddiagramelementcontainer() {
        return diagram_ddiagramelementcontainer;
    }

    public void setDiagram_ddiagramelementcontainer(diagram_DDiagramElementContainer diagram_ddiagramelementcontainer) {
        this.diagram_ddiagramelementcontainer = diagram_ddiagramelementcontainer;
    }
    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }

}