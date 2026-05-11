





import java.util.List;
import java.util.ArrayList;

public class geoff_XYZLocation extends Location {

    private float y;
    private float z;
    private float x;



    public geoff_XYZLocation(
        float y,        float z,        float x    ) {
        super(
        );
        this.y = y;
        this.z = z;
        this.x = x;
    }


    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }
    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
    }
    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }


}