





import java.util.List;
import java.util.ArrayList;

public class model_Size extends Feature {

    private boolean resizable;
    private int height;
    private boolean widthRelative;
    private int width;
    private boolean heightRelative;



    public model_Size(
        boolean resizable,        int height,        boolean widthRelative,        int width,        boolean heightRelative    ) {
        super(
        );
        this.resizable = resizable;
        this.height = height;
        this.widthRelative = widthRelative;
        this.width = width;
        this.heightRelative = heightRelative;
    }


    public boolean getResizable() {
        return resizable;
    }

    public void setResizable(boolean resizable) {
        this.resizable = resizable;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public boolean getWidthrelative() {
        return widthRelative;
    }

    public void setWidthrelative(boolean widthRelative) {
        this.widthRelative = widthRelative;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public boolean getHeightrelative() {
        return heightRelative;
    }

    public void setHeightrelative(boolean heightRelative) {
        this.heightRelative = heightRelative;
    }


}