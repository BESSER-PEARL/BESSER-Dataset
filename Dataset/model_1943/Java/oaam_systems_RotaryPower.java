





import java.util.List;
import java.util.ArrayList;

public class oaam_systems_RotaryPower extends InformationPower {

    private float angularVelocity;
    private float momentum;



    public oaam_systems_RotaryPower(
        float angularVelocity,        float momentum    ) {
        super(
        );
        this.angularVelocity = angularVelocity;
        this.momentum = momentum;
    }


    public float getAngularvelocity() {
        return angularVelocity;
    }

    public void setAngularvelocity(float angularVelocity) {
        this.angularVelocity = angularVelocity;
    }
    public float getMomentum() {
        return momentum;
    }

    public void setMomentum(float momentum) {
        this.momentum = momentum;
    }


}