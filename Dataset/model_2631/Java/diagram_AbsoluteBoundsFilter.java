





import java.util.List;
import java.util.ArrayList;

public class diagram_AbsoluteBoundsFilter extends GraphicalFilter {

    private String x;
    private String width;
    private String y;
    private String height;



    public diagram_AbsoluteBoundsFilter(
        String x,        String width,        String y,        String height    ) {
        super(
        );
        this.x = x;
        this.width = width;
        this.y = y;
        this.height = height;
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
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }


}