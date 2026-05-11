





import java.util.List;
import java.util.ArrayList;

public class qm_LinearFunction extends Function {

    private float lowerBound;
    private float upperBound;



    public qm_LinearFunction(
        float lowerBound,        float upperBound    ) {
        super(
        );
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public float getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(float lowerBound) {
        this.lowerBound = lowerBound;
    }
    public float getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(float upperBound) {
        this.upperBound = upperBound;
    }


}