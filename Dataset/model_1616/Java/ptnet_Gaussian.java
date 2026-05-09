





import java.util.List;
import java.util.ArrayList;

public class ptnet_Gaussian extends Distribution {

    private float Variance;
    private float Mean;



    public ptnet_Gaussian(
        float Variance,        float Mean    ) {
        super(
        );
        this.Variance = Variance;
        this.Mean = Mean;
    }


    public float getVariance() {
        return Variance;
    }

    public void setVariance(float Variance) {
        this.Variance = Variance;
    }
    public float getMean() {
        return Mean;
    }

    public void setMean(float Mean) {
        this.Mean = Mean;
    }


}