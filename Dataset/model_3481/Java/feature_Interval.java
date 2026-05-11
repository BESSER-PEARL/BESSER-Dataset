





import java.util.List;
import java.util.ArrayList;

public class feature_Interval  {

    private int upperBound;
    private int lowerBound;





    private feature_NumericalDomain feature_numericaldomain;


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

    public feature_NumericalDomain getFeature_numericaldomain() {
        return feature_numericaldomain;
    }

    public void setFeature_numericaldomain(feature_NumericalDomain feature_numericaldomain) {
        this.feature_numericaldomain = feature_numericaldomain;
    }

}