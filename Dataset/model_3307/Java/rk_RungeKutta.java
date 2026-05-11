





import java.util.List;
import java.util.ArrayList;

public class rk_RungeKutta extends Solver {

    private float relativeTolerance;



    public rk_RungeKutta(
        float relativeTolerance    ) {
        super(
        );
        this.relativeTolerance = relativeTolerance;
    }


    public float getRelativetolerance() {
        return relativeTolerance;
    }

    public void setRelativetolerance(float relativeTolerance) {
        this.relativeTolerance = relativeTolerance;
    }


}