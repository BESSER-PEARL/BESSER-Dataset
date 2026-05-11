





import java.util.List;
import java.util.ArrayList;

public class xDrone_Vector  {

    private String z;
    private String x;
    private String y;





    private xDrone_Size xdrone_size;




    private xDrone_Origin xdrone_origin;


    public xDrone_Vector(
        String z,        String x,        String y    ) {
        this.z = z;
        this.x = x;
        this.y = y;
    }


    public String getZ() {
        return z;
    }

    public void setZ(String z) {
        this.z = z;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }

    public xDrone_Size getXdrone_size() {
        return xdrone_size;
    }

    public void setXdrone_size(xDrone_Size xdrone_size) {
        this.xdrone_size = xdrone_size;
    }
    public xDrone_Origin getXdrone_origin() {
        return xdrone_origin;
    }

    public void setXdrone_origin(xDrone_Origin xdrone_origin) {
        this.xdrone_origin = xdrone_origin;
    }

}