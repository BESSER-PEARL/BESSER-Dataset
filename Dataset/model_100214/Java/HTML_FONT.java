





import java.util.List;
import java.util.ArrayList;

public class HTML_FONT extends BODYElement {

    private String color;
    private String face;
    private String size;



    public HTML_FONT(
        String color,        String face,        String size    ) {
        super(
        );
        this.color = color;
        this.face = face;
        this.size = size;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getFace() {
        return face;
    }

    public void setFace(String face) {
        this.face = face;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}