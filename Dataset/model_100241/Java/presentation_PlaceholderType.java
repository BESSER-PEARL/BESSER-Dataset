





import java.util.List;
import java.util.ArrayList;

public class presentation_PlaceholderType  {

    private String x;
    private String object;
    private String width;
    private String y;
    private String height;



    public presentation_PlaceholderType(
        String x,        String object,        String width,        String y,        String height    ) {
        this.x = x;
        this.object = object;
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
    public String getObject() {
        return object;
    }

    public void setObject(String object) {
        this.object = object;
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