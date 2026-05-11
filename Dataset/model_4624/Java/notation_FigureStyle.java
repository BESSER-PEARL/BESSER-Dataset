





import java.util.List;
import java.util.ArrayList;

public class notation_FigureStyle extends Style {

    private float height;
    private String fillOrientation;
    private int brightness;
    private String fillTexture;
    private String orientation;
    private float width;
    private String fillColor;
    private String fillTextureColor;





    private notation_Figure notation_figure;


    public notation_FigureStyle(
        float height,        String fillOrientation,        int brightness,        String fillTexture,        String orientation,        float width,        String fillColor,        String fillTextureColor    ) {
        super(
        );
        this.height = height;
        this.fillOrientation = fillOrientation;
        this.brightness = brightness;
        this.fillTexture = fillTexture;
        this.orientation = orientation;
        this.width = width;
        this.fillColor = fillColor;
        this.fillTextureColor = fillTextureColor;
    }


    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }
    public String getFillorientation() {
        return fillOrientation;
    }

    public void setFillorientation(String fillOrientation) {
        this.fillOrientation = fillOrientation;
    }
    public int getBrightness() {
        return brightness;
    }

    public void setBrightness(int brightness) {
        this.brightness = brightness;
    }
    public String getFilltexture() {
        return fillTexture;
    }

    public void setFilltexture(String fillTexture) {
        this.fillTexture = fillTexture;
    }
    public String getOrientation() {
        return orientation;
    }

    public void setOrientation(String orientation) {
        this.orientation = orientation;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public String getFillcolor() {
        return fillColor;
    }

    public void setFillcolor(String fillColor) {
        this.fillColor = fillColor;
    }
    public String getFilltexturecolor() {
        return fillTextureColor;
    }

    public void setFilltexturecolor(String fillTextureColor) {
        this.fillTextureColor = fillTextureColor;
    }

    public notation_Figure getNotation_figure() {
        return notation_figure;
    }

    public void setNotation_figure(notation_Figure notation_figure) {
        this.notation_figure = notation_figure;
    }

}