





import java.util.List;
import java.util.ArrayList;

public class drones_SizedElement  {

    private float z;
    private float length;
    private float width;
    private float y;
    private float x;
    private float height;



    public drones_SizedElement(
        float z,        float length,        float width,        float y,        float x,        float height    ) {
        this.z = z;
        this.length = length;
        this.width = width;
        this.y = y;
        this.x = x;
        this.height = height;
    }


    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }
    public float getLength() {
        return length;
    }

    public void setLength(float length) {
        this.length = length;
    }
    public float getWidth() {
        return width;
    }

    public void setWidth(float width) {
        this.width = width;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getHeight() {
        return height;
    }

    public void setHeight(float height) {
        this.height = height;
    }


}