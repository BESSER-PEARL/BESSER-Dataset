





import java.util.List;
import java.util.ArrayList;

public class FCORE_SolitaryFeature extends Feature {

    private int min;
    private int max;





    private FCORE_FeatureModel fcore_featuremodel;


    public FCORE_SolitaryFeature(
        int min,        int max    ) {
        super(
        );
        this.min = min;
        this.max = max;
    }


    public int getMin() {
        return min;
    }

    public void setMin(int min) {
        this.min = min;
    }
    public int getMax() {
        return max;
    }

    public void setMax(int max) {
        this.max = max;
    }

    public FCORE_FeatureModel getFcore_featuremodel() {
        return fcore_featuremodel;
    }

    public void setFcore_featuremodel(FCORE_FeatureModel fcore_featuremodel) {
        this.fcore_featuremodel = fcore_featuremodel;
    }

}