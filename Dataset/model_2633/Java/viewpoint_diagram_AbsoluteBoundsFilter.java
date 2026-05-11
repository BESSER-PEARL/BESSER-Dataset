





import java.util.List;
import java.util.ArrayList;

public class viewpoint_diagram_AbsoluteBoundsFilter extends GraphicalFilter {

    private String height;
    private String y;
    private String width;
    private String x;



    public viewpoint_diagram_AbsoluteBoundsFilter(
        String height,        String y,        String width,        String x    ) {
        super(
        );
        this.height = height;
        this.y = y;
        this.width = width;
        this.x = x;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }


}