





import java.util.List;
import java.util.ArrayList;

public class graphgenerators_PlateCarreeGlobeGraphGenerator extends LatticeGraphGenerator {

    private float radius;
    private int angularStep;



    public graphgenerators_PlateCarreeGlobeGraphGenerator(
        float radius,        int angularStep    ) {
        super(
        );
        this.radius = radius;
        this.angularStep = angularStep;
    }


    public float getRadius() {
        return radius;
    }

    public void setRadius(float radius) {
        this.radius = radius;
    }
    public int getAngularstep() {
        return angularStep;
    }

    public void setAngularstep(int angularStep) {
        this.angularStep = angularStep;
    }


}