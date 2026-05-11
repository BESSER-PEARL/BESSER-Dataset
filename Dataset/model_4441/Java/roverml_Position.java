





import java.util.List;
import java.util.ArrayList;

public class roverml_Position extends Quantity {

    private float x;
    private float y;





    private roverml_GPSTrigger roverml_gpstrigger;


    public roverml_Position(
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

    public roverml_GPSTrigger getRoverml_gpstrigger() {
        return roverml_gpstrigger;
    }

    public void setRoverml_gpstrigger(roverml_GPSTrigger roverml_gpstrigger) {
        this.roverml_gpstrigger = roverml_gpstrigger;
    }

}