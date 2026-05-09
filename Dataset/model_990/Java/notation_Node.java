





import java.util.List;
import java.util.ArrayList;

public class notation_Node extends DiagramElement {

    private int width;
    private int y;
    private int height;
    private int x;



    public notation_Node(
        int width,        int y,        int height,        int x    ) {
        super(
        );
        this.width = width;
        this.y = y;
        this.height = height;
        this.x = x;
    }


    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
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


}