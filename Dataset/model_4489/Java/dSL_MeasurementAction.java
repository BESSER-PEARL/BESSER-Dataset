





import java.util.List;
import java.util.ArrayList;

public class dSL_MeasurementAction extends Actions {

    private String measure;



    public dSL_MeasurementAction(
        String measure    ) {
        super(
        );
        this.measure = measure;
    }


    public String getMeasure() {
        return measure;
    }

    public void setMeasure(String measure) {
        this.measure = measure;
    }


}