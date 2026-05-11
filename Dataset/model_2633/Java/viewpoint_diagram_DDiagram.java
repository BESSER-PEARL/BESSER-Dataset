





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_DDiagram extends DragAndDropTarget, description_DocumentedElement, DValidable, DContainer, DRepresentation {

    private boolean isInLayoutingMode;
    private String info;
    private boolean synchronized;
    private int headerHeight;



    public viewpoint_diagram_DDiagram(
        boolean isInLayoutingMode,        String info,        boolean synchronized,        int headerHeight    ) {
        super(
        );
        this.isInLayoutingMode = isInLayoutingMode;
        this.info = info;
        this.synchronized = synchronized;
        this.headerHeight = headerHeight;
    }


    public boolean getIsinlayoutingmode() {
        return isInLayoutingMode;
    }

    public void setIsinlayoutingmode(boolean isInLayoutingMode) {
        this.isInLayoutingMode = isInLayoutingMode;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public int getHeaderheight() {
        return headerHeight;
    }

    public void setHeaderheight(int headerHeight) {
        this.headerHeight = headerHeight;
    }


}