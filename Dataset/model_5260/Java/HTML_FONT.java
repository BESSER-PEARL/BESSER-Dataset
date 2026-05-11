





import java.util.List;
import java.util.ArrayList;

public class HTML_FONT extends HTMLElement {

    private String color;
    private String value;
    private String face;
    private String size;



    public HTML_FONT(
        String color,        String value,        String face,        String size    ) {
        super(
        );
        this.color = color;
        this.value = value;
        this.face = face;
        this.size = size;
    }


    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
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