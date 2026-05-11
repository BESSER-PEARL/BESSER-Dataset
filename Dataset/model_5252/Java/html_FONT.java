





import java.util.List;
import java.util.ArrayList;

public class html_FONT extends BODYElement {

    private String size;
    private String color;
    private String face;



    public html_FONT(
        String size,        String color,        String face    ) {
        super(
        );
        this.size = size;
        this.color = color;
        this.face = face;
    }


    public String getSize() {
        return size;
    }

    public void setSize(String size) {
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


}