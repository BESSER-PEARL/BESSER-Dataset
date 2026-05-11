





import java.util.List;
import java.util.ArrayList;

public class feature_Interval  {

    private int lowerBound;
    private int upperBound;





    private feature_ContinuousDomain feature_continuousdomain;


    public feature_Interval(
        int lowerBound,        int upperBound    ) {
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
    }


    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }

    public feature_ContinuousDomain getFeature_continuousdomain() {
        return feature_continuousdomain;
    }

    public void setFeature_continuousdomain(feature_ContinuousDomain feature_continuousdomain) {
        this.feature_continuousdomain = feature_continuousdomain;
    }

}