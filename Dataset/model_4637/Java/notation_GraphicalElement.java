





import java.util.List;
import java.util.ArrayList;

public class notation_GraphicalElement extends NotationElement {

    private int width;
    private int height;
    private int x;
    private String stroke;
    private int y;
    private String fill;



    public notation_GraphicalElement(
        int width,        int height,        int x,        String stroke,        int y,        String fill    ) {
        super(
        );
        this.width = width;
        this.height = height;
        this.x = x;
        this.stroke = stroke;
        this.y = y;
        this.fill = fill;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public String getStroke() {
        return stroke;
    }

    public void setStroke(String stroke) {
        this.stroke = stroke;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public String getFill() {
        return fill;
    }

    public void setFill(String fill) {
        this.fill = fill;
    }


}