





import java.util.List;
import java.util.ArrayList;

public class roverml_Move extends Command {

    private float velocity;
    private float length;





    private roverml_Velocity roverml_velocity;


    public roverml_Move(
        float velocity,        float length    ) {
        super(
        );
        this.velocity = velocity;
        this.length = length;
    }


    public float getVelocity() {
        return velocity;
    }

    public void setVelocity(float velocity) {
        this.velocity = velocity;
    }
    public float getLength() {
        return length;
    }

    public void setLength(float length) {
        this.length = length;
    }

    public roverml_Velocity getRoverml_velocity() {
        return roverml_velocity;
    }

    public void setRoverml_velocity(roverml_Velocity roverml_velocity) {
        this.roverml_velocity = roverml_velocity;
    }

}