





import java.util.List;
import java.util.ArrayList;

public class model_ListSupport  {

    private boolean horizontalLines;
    private int rowHeight;



    public model_ListSupport(
        boolean horizontalLines,        int rowHeight    ) {
        this.horizontalLines = horizontalLines;
        this.rowHeight = rowHeight;
    }


    public boolean getHorizontallines() {
        return horizontalLines;
    }

    public void setHorizontallines(boolean horizontalLines) {
        this.horizontalLines = horizontalLines;
    }
    public int getRowheight() {
        return rowHeight;
    }

    public void setRowheight(int rowHeight) {
        this.rowHeight = rowHeight;
    }


}