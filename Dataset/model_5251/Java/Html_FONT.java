





import java.util.List;
import java.util.ArrayList;

public class Html_FONT extends BODYElement {

    private String face;
    private String color;
    private String size;



    public Html_FONT(
        String face,        String color,        String size    ) {
        super(
        );
        this.face = face;
        this.color = color;
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
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }


}