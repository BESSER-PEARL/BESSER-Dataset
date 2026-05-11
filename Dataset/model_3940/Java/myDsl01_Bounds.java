





import java.util.List;
import java.util.ArrayList;

public class myDsl01_Bounds  {

    private int width;
    private int y;
    private int height;
    private int x;





    private myDsl01_UIElement mydsl01_uielement;


    public myDsl01_Bounds(
        int width,        int y,        int height,        int x    ) {
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

    public myDsl01_UIElement getMydsl01_uielement() {
        return mydsl01_uielement;
    }

    public void setMydsl01_uielement(myDsl01_UIElement mydsl01_uielement) {
        this.mydsl01_uielement = mydsl01_uielement;
    }

}