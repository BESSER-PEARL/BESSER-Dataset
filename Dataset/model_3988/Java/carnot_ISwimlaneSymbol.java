





import java.util.List;
import java.util.ArrayList;

public class carnot_ISwimlaneSymbol extends IIdentifiableElement, INodeSymbol {

    private String orientation;
    private String collapsed;



    public carnot_ISwimlaneSymbol(
        String orientation,        String collapsed    ) {
        super(
        );
        this.orientation = orientation;
        this.collapsed = collapsed;
    }


    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getCollapsed() {
        return collapsed;
    }

    public void setCollapsed(String collapsed) {
        this.collapsed = collapsed;
    }


}