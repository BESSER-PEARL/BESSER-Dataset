





import java.util.List;
import java.util.ArrayList;

public class HTML_FONT extends BODYElement {

    private String size;
    private String face;
    private String color;



    public HTML_FONT(
        String size,        String face,        String color    ) {
        super(
        );
        this.size = size;
        this.face = face;
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
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }


}