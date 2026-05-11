





import java.util.List;
import java.util.ArrayList;

public class eel_MeasurementUncertainty  {

    private String standardUncertainty;





    private eel_Measure eel_measure;


    public eel_MeasurementUncertainty(
        String standardUncertainty    ) {
        this.standardUncertainty = standardUncertainty;
    }


    public String getStandarduncertainty() {
        return standardUncertainty;
    }

    public void setStandarduncertainty(String standardUncertainty) {
        this.standardUncertainty = standardUncertainty;
    }

    public eel_Measure getEel_measure() {
        return eel_measure;
    }

    public void setEel_measure(eel_Measure eel_measure) {
        this.eel_measure = eel_measure;
    }

}