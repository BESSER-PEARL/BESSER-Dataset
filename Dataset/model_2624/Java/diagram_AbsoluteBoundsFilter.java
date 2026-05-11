





import java.util.List;
import java.util.ArrayList;

public class diagram_AbsoluteBoundsFilter extends GraphicalFilter {

    private String height;
    private String width;
    private String x;
    private String y;



    public diagram_AbsoluteBoundsFilter(
        String height,        String width,        String x,        String y    ) {
        super(
        );
        this.height = height;
        this.width = width;
        this.x = x;
        this.y = y;
    }


    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
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
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }


}