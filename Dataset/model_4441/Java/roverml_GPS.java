





import java.util.List;
import java.util.ArrayList;

public class roverml_GPS extends Sensor {

    private float x;
    private float y;



    public roverml_GPS(
        float x,        float y    ) {
        super(
        );
        this.x = x;
        this.y = y;
    }


    public float getX() {
        return x;
    }

    public void setX(float x) {
        this.x = x;
    }
    public float getY() {
        return y;
    }

    public void setY(float y) {
        this.y = y;
    }


}