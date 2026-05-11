





import java.util.List;
import java.util.ArrayList;

public class notation_Size extends LayoutConstraint {

    private int width;
    private int height;



    public notation_Size(
        int width,        int height    ) {
        super(
        );
        this.width = width;
        this.height = height;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }


}