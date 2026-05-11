





import java.util.List;
import java.util.ArrayList;

public class swt_FormData extends LayoutData {

    private int height;
    private int width;



    public swt_FormData(
        int height,        int width    ) {
        super(
        );
        this.height = height;
        this.width = width;
    }


    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }


}