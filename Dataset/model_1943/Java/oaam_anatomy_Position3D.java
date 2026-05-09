





import java.util.List;
import java.util.ArrayList;

public class oaam_anatomy_Position3D extends common_OaamBaseElementA, scenario_ModeDependentElementA, scenario_VariantDependentElementA {

    private float z;
    private float y;
    private float x;



    public oaam_anatomy_Position3D(
        float z,        float y,        float x    ) {
        super(
        );
        this.z = z;
        this.y = y;
        this.x = x;
    }


    public float getZ() {
        return z;
    }

    public void setZ(float z) {
        this.z = z;
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


}