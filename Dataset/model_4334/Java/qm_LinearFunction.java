





import java.util.List;
import java.util.ArrayList;

public class qm_LinearFunction extends Function {

    private float upperBound;
    private float lowerBound;



    public qm_LinearFunction(
        float upperBound,        float lowerBound    ) {
        super(
        );
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
    }


    public float getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(float upperBound) {
        this.upperBound = upperBound;
    }
    public float getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(float lowerBound) {
        this.lowerBound = lowerBound;
    }


}