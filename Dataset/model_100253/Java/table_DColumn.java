





import java.util.List;
import java.util.ArrayList;

public class table_DColumn extends DTableElement {

    private String label;
    private boolean visible;
    private int width;





    private table_DTable table_dtable;




    private table_DTable table_dtable;


    public table_DColumn(
        String label,        boolean visible,        int width    ) {
        super(
        );
        this.label = label;
        this.visible = visible;
        this.width = width;
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
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }

    public table_DTable getTable_dtable() {
        return table_dtable;
    }

    public void setTable_dtable(table_DTable table_dtable) {
        this.table_dtable = table_dtable;
    }
    public table_DTable getTable_dtable() {
        return table_dtable;
    }

    public void setTable_dtable(table_DTable table_dtable) {
        this.table_dtable = table_dtable;
    }

}