





import java.util.List;
import java.util.ArrayList;

public class dc_Bounds  {

    private String height;
    private String width;
    private String y;
    private String x;



    public dc_Bounds(
        String height,        String width,        String y,        String x    ) {
        this.height = height;
        this.width = width;
        this.y = y;
        this.x = x;
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


}