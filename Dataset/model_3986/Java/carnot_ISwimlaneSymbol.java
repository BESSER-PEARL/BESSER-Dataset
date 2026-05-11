





import java.util.List;
import java.util.ArrayList;

public class carnot_ISwimlaneSymbol extends INodeSymbol, IIdentifiableElement {

    private String collapsed;
    private String orientation;



    public carnot_ISwimlaneSymbol(
        String collapsed,        String orientation    ) {
        super(
        );
        this.collapsed = collapsed;
        this.orientation = orientation;
    }


    public String getCollapsed() {
        return collapsed;
    }

    public void setCollapsed(String collapsed) {
        this.collapsed = collapsed;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }


}