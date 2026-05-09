





import java.util.List;
import java.util.ArrayList;

public class oaam_systems_LinearPower extends InformationPower {

    private float force;
    private float velocity;



    public oaam_systems_LinearPower(
        float force,        float velocity    ) {
        super(
        );
        this.force = force;
        this.velocity = velocity;
    }


    public float getForce() {
        return force;
    }

    public void setForce(float force) {
        this.force = force;
    }
    public float getVelocity() {
        return velocity;
    }

    public void setVelocity(float velocity) {
        this.velocity = velocity;
    }


}