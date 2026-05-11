





import java.util.List;
import java.util.ArrayList;

public class notation_GraphicalElement extends NotationElement {

    private int y;
    private int x;
    private int width;
    private String stroke;
    private String fill;
    private int height;



    public notation_GraphicalElement(
        int y,        int x,        int width,        String stroke,        String fill,        int height    ) {
        super(
        );
        this.y = y;
        this.x = x;
        this.width = width;
        this.stroke = stroke;
        this.fill = fill;
        this.height = height;
    }


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public String getStroke() {
        return stroke;
    }

    public void setStroke(String stroke) {
        this.stroke = stroke;
    }
    public String getFill() {
        return fill;
    }

    public void setFill(String fill) {
        this.fill = fill;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }


}