





import java.util.List;
import java.util.ArrayList;

public class diagram_DDiagram extends description_DocumentedElement, DragAndDropTarget, DRepresentation {

    private int headerHeight;
    private boolean synchronized;
    private boolean isInLayoutingMode;



    public diagram_DDiagram(
        int headerHeight,        boolean synchronized,        boolean isInLayoutingMode    ) {
        super(
        );
        this.headerHeight = headerHeight;
        this.synchronized = synchronized;
        this.isInLayoutingMode = isInLayoutingMode;
    }


    public int getHeaderheight() {
        return headerHeight;
    }

    public void setHeaderheight(int headerHeight) {
        this.headerHeight = headerHeight;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getIsinlayoutingmode() {
        return isInLayoutingMode;
    }

    public void setIsinlayoutingmode(boolean isInLayoutingMode) {
        this.isInLayoutingMode = isInLayoutingMode;
    }


}