





import java.util.List;
import java.util.ArrayList;

public class di_Shape extends ContainerShape {

    private int y;
    private int width;
    private int x;
    private int height;



    public di_Shape(
        int y,        int width,        int x,        int height    ) {
        super(
        );
        this.y = y;
        this.width = width;
        this.x = x;
        this.height = height;
    }


    public int getY() {
        return y;
    }

    public void setY(int y) {
        this.y = y;
    }
    public int getWidth() {
        return width;
    }

    public void setWidth(int width) {
        this.width = width;
    }
    public int getX() {
        return x;
    }

    public void setX(int x) {
        this.x = x;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }


}