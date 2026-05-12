





import java.util.List;
import java.util.ArrayList;

public class table_DLine extends LineContainer, DTableElement {

    private boolean collapsed;
    private String label;
    private boolean visible;



    public table_DLine(
        boolean collapsed,        String label,        boolean visible    ) {
        super(
        );
        this.collapsed = collapsed;
        this.label = label;
        this.visible = visible;
    }


    public boolean getCollapsed() {
        return collapsed;
    }

    public void setCollapsed(boolean collapsed) {
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


}