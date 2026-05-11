





import java.util.List;
import java.util.ArrayList;

public class eel_NormalDistribution extends MeasurementUncertaintyInformation {

    private String standardDeviation;
    private String meanValue;



    public eel_NormalDistribution(
        String standardDeviation,        String meanValue    ) {
        super(
        );
        this.standardDeviation = standardDeviation;
        this.meanValue = meanValue;
    }


    public String getStandarddeviation() {
        return standardDeviation;
    }

    public void setStandarddeviation(String standardDeviation) {
        this.standardDeviation = standardDeviation;
    }
    public String getMeanvalue() {
        return meanValue;
    }

    public void setMeanvalue(String meanValue) {
        this.meanValue = meanValue;
    }


}