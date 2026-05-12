





import java.util.List;
import java.util.ArrayList;

public class HTML_FONT extends BODYElement {

    private String color;
    private String size;
    private String face;



    public HTML_FONT(
        String color,        String size,        String face    ) {
        super(
        );
        this.color = color;
        this.size = size;
        this.face = face;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getFace() {
        return face;
    }

    public void setFace(String face) {
        this.face = face;
    }


}