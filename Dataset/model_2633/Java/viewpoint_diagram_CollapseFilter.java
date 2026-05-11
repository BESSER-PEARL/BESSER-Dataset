





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_CollapseFilter extends GraphicalFilter {

    private int width;
    private int height;



    public viewpoint_diagram_CollapseFilter(
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