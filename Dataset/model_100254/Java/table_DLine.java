





import java.util.List;
import java.util.ArrayList;

public class table_DLine extends DTableElement, LineContainer, DTableElementUpdater {

    private String label;
    private boolean visible;
    private boolean collapsed;



    public table_DLine(
        String label,        boolean visible,        boolean collapsed    ) {
        super(
        );
        this.label = label;
        this.visible = visible;
        this.collapsed = collapsed;
    }


    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public boolean getCollapsed() {
        return collapsed;
    }

    public void setCollapsed(boolean collapsed) {
        this.collapsed = collapsed;
    }


}