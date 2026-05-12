





import java.util.List;
import java.util.ArrayList;

public class table_DColumn extends DTableElement {

    private boolean visible;
    private String label;
    private int width;



    public table_DColumn(
        boolean visible,        String label,        int width    ) {
        super(
        );
        this.visible = visible;
        this.label = label;
        this.width = width;
    }


    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }


}