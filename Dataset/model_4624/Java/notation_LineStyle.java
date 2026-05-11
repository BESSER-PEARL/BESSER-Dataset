





import java.util.List;
import java.util.ArrayList;

public class notation_LineStyle extends Style {

    private String orientation;
    private String texture;
    private float length;
    private int brightness;
    private String color;
    private float thickness;





    private notation_Line notation_line;


    public notation_LineStyle(
        String orientation,        String texture,        float length,        int brightness,        String color,        float thickness    ) {
        super(
        );
        this.orientation = orientation;
        this.texture = texture;
        this.length = length;
        this.brightness = brightness;
        this.color = color;
        this.thickness = thickness;
    }


    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public String getTexture() {
        return texture;
    }

    public void setTexture(String texture) {
        this.texture = texture;
    }
    public float getLength() {
        return length;
    }

    public void setLength(float length) {
        this.length = length;
    }
    public int getBrightness() {
        return brightness;
    }

    public void setBrightness(int brightness) {
        this.brightness = brightness;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public float getThickness() {
        return thickness;
    }

    public void setThickness(float thickness) {
        this.thickness = thickness;
    }

    public notation_Line getNotation_line() {
        return notation_line;
    }

    public void setNotation_line(notation_Line notation_line) {
        this.notation_line = notation_line;
    }

}