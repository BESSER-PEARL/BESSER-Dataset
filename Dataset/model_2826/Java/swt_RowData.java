





import java.util.List;
import java.util.ArrayList;

public class swt_RowData extends LayoutData {

    private int height;
    private boolean exclude;
    private int width;



    public swt_RowData(
        int height,        boolean exclude,        int width    ) {
        super(
        );
        this.height = height;
        this.exclude = exclude;
        this.width = width;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public boolean getExclude() {
        return exclude;
    }

    public void setExclude(boolean exclude) {
        this.exclude = exclude;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }


}