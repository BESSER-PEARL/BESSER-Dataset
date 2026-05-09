





import java.util.List;
import java.util.ArrayList;

public class dc_Bounds  {

    private String x;
    private String height;
    private String width;
    private String y;



    public dc_Bounds(
        String x,        String height,        String width,        String y    ) {
        this.x = x;
        this.height = height;
        this.width = width;
        this.y = y;
    }


    public String getX() {
        return x;
    }

    public void setX(String x) {
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


}