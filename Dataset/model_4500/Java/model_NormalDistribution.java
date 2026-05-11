





import java.util.List;
import java.util.ArrayList;

public class model_NormalDistribution extends MeasurementUncertaintyInformation {

    private float meanValue;
    private float standardDeviation;



    public model_NormalDistribution(
        float meanValue,        float standardDeviation    ) {
        super(
        );
        this.meanValue = meanValue;
        this.standardDeviation = standardDeviation;
    }


    public float getMeanvalue() {
        return meanValue;
    }

    public void setMeanvalue(float meanValue) {
        this.meanValue = meanValue;
    }
    public float getStandarddeviation() {
        return standardDeviation;
    }

    public void setStandarddeviation(float standardDeviation) {
        this.standardDeviation = standardDeviation;
    }


}