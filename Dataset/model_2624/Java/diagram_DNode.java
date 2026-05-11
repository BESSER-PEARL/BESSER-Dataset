





import java.util.List;
import java.util.ArrayList;

public class diagram_DNode extends AbstractDNode, DragAndDropTarget, EdgeTarget {

    private String labelPosition;
    private String height;
    private String resizeKind;
    private String width;





    private diagram_DDiagram diagram_ddiagram;


    public diagram_DNode(
        String labelPosition,        String height,        String resizeKind,        String width    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.height = height;
        this.resizeKind = resizeKind;
        this.width = width;
    }


    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getResizekind() {
        return resizeKind;
    }

    public void setResizekind(String resizeKind) {
        this.resizeKind = resizeKind;
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

}