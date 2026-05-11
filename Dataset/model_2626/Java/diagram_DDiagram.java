





import java.util.List;
import java.util.ArrayList;

public class diagram_DDiagram extends DragAndDropTarget, description_DocumentedElement, DRepresentation {

    private int headerHeight;
    private boolean isInLayoutingMode;
    private boolean synchronized;



    public diagram_DDiagram(
        int headerHeight,        boolean isInLayoutingMode,        boolean synchronized    ) {
        super(
        );
        this.headerHeight = headerHeight;
        this.isInLayoutingMode = isInLayoutingMode;
        this.synchronized = synchronized;
    }


    public int getHeaderheight() {
        return headerHeight;
    }

    public void setHeaderheight(int headerHeight) {
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


}