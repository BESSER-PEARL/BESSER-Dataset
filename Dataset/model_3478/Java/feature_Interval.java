





import java.util.List;
import java.util.ArrayList;

public class feature_Interval  {

    private int upperBound;
    private int lowerBound;





    private feature_ContinuousDomain feature_continuousdomain;


    public feature_Interval(
        int upperBound,        int lowerBound    ) {
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
    }


    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }

    public feature_ContinuousDomain getFeature_continuousdomain() {
        return feature_continuousdomain;
    }

    public void setFeature_continuousdomain(feature_ContinuousDomain feature_continuousdomain) {
        this.feature_continuousdomain = feature_continuousdomain;
    }

}