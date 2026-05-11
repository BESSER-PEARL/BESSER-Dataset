





import java.util.List;
import java.util.ArrayList;

public class diagram_DNode extends EdgeTarget, AbstractDNode, DragAndDropTarget {

    private String labelPosition;
    private String width;
    private String resizeKind;
    private String height;





    private diagram_DDiagram diagram_ddiagram;


    public diagram_DNode(
        String labelPosition,        String width,        String resizeKind,        String height    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.width = width;
        this.resizeKind = resizeKind;
        this.height = height;
    }


    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
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

    public diagram_DDiagram getDiagram_ddiagram() {
        return diagram_ddiagram;
    }

    public void setDiagram_ddiagram(diagram_DDiagram diagram_ddiagram) {
        this.diagram_ddiagram = diagram_ddiagram;
    }

}