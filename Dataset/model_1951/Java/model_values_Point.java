





import java.util.List;
import java.util.ArrayList;

public class model_values_Point extends Value {

    private String y;
    private String x;
    private String z;



    public model_values_Point(
        String y,        String x,        String z    ) {
        super(
        );
        this.y = y;
        this.x = x;
        this.z = z;
    }


    public String getY() {
        return y;
    }

    public void setY(String y) {
        this.y = y;
    }
    public String getX() {
        return x;
    }

    public void setX(String x) {
        this.x = x;
    }
    public String getZ() {
        return z;
    }

    public void setZ(String z) {
        this.z = z;
    }


}