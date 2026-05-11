





import java.util.List;
import java.util.ArrayList;

public class notation_BorderStyle extends Style {

    private float thickness;
    private String texture;
    private String color;





    private notation_Figure notation_figure;


    public notation_BorderStyle(
        float thickness,        String texture,        String color    ) {
        super(
        );
        this.thickness = thickness;
        this.texture = texture;
        this.color = color;
    }


    public float getThickness() {
        return thickness;
    }

    public void setThickness(float thickness) {
        this.thickness = thickness;
    }
    public String getTexture() {
        return texture;
    }

    public void setTexture(String texture) {
        this.texture = texture;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public notation_Figure getNotation_figure() {
        return notation_figure;
    }

    public void setNotation_figure(notation_Figure notation_figure) {
        this.notation_figure = notation_figure;
    }

}