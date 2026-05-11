





import java.util.List;
import java.util.ArrayList;

public class diagram_DDiagram extends DRepresentation, description_DocumentedElement, DragAndDropTarget {

    private boolean isInLayoutingMode;
    private boolean synchronized;
    private int headerHeight;



    public diagram_DDiagram(
        boolean isInLayoutingMode,        boolean synchronized,        int headerHeight    ) {
        super(
        );
        this.isInLayoutingMode = isInLayoutingMode;
        this.synchronized = synchronized;
        this.headerHeight = headerHeight;
    }


    public boolean getIsinlayoutingmode() {
        return isInLayoutingMode;
    }

    public void setIsinlayoutingmode(boolean isInLayoutingMode) {
        this.isInLayoutingMode = isInLayoutingMode;
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