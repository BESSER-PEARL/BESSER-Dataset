





import java.util.List;
import java.util.ArrayList;

public class notation_IconStyle extends Style {

    private int brightness;
    private float height;
    private float width;
    private String orientation;
    private String color;





    private notation_Icon notation_icon;


    public notation_IconStyle(
        int brightness,        float height,        float width,        String orientation,        String color    ) {
        super(
        );
        this.brightness = brightness;
        this.height = height;
        this.width = width;
        this.orientation = orientation;
        this.color = color;
    }


    public int getBrightness() {
        return brightness;
    }

    public void setBrightness(int brightness) {
        this.brightness = brightness;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public notation_Icon getNotation_icon() {
        return notation_icon;
    }

    public void setNotation_icon(notation_Icon notation_icon) {
        this.notation_icon = notation_icon;
    }

}