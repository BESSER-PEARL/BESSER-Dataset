





import java.util.List;
import java.util.ArrayList;

public class graphbt_Layout  {

    private int width;
    private int y;
    private String cRef;
    private int x;
    private int height;
    private int z;



    public graphbt_Layout(
        int width,        int y,        String cRef,        int x,        int height,        int z    ) {
        this.width = width;
        this.y = y;
        this.cRef = cRef;
        this.x = x;
        this.height = height;
        this.z = z;
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
    public String getCref() {
        return cRef;
    }

    public void setCref(String cRef) {
        this.cRef = cRef;
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
    public int getZ() {
        return z;
    }

    public void setZ(int z) {
        this.z = z;
    }


}