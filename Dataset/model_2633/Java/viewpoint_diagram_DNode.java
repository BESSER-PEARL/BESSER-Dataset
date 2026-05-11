





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DNode extends diagram_EdgeTarget, DragAndDropTarget, diagram_AbstractDNode {

    private String labelPosition;
    private String height;
    private String width;
    private String resizeKind;



    public viewpoint_diagram_DNode(
        String labelPosition,        String height,        String width,        String resizeKind    ) {
        super(
        );
        this.labelPosition = labelPosition;
        this.height = height;
        this.width = width;
        this.resizeKind = resizeKind;
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


}