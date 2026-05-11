





import java.util.List;
import java.util.ArrayList;

public class diagram_AbsoluteBoundsFilter extends GraphicalFilter {

    private String height;
    private String y;
    private String x;
    private String width;



    public diagram_AbsoluteBoundsFilter(
        String height,        String y,        String x,        String width    ) {
        super(
        );
        this.height = height;
        this.y = y;
        this.x = x;
        this.width = width;
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
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getWidth() {
        return width;
    }

    public void setWidth(String width) {
        this.width = width;
    }


}