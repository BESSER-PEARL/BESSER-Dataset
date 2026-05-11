





import java.util.List;
import java.util.ArrayList;

public class model_Sampling extends MeasurementUncertaintyInformation {

    private String measurementProcedure;



    public model_Sampling(
        String measurementProcedure    ) {
        super(
        );
        this.measurementProcedure = measurementProcedure;
    }


    public String getMeasurementprocedure() {
        return measurementProcedure;
    }

    public void setMeasurementprocedure(String measurementProcedure) {
        this.measurementProcedure = measurementProcedure;
    }


}