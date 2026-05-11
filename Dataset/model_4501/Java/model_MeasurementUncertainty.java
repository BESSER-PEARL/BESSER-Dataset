





import java.util.List;
import java.util.ArrayList;

public class model_MeasurementUncertainty  {

    private float standardUncertainty;



    public model_MeasurementUncertainty(
        float standardUncertainty    ) {
        this.standardUncertainty = standardUncertainty;
    }


    public float getStandarduncertainty() {
        return standardUncertainty;
    }

    public void setStandarduncertainty(float standardUncertainty) {
        this.standardUncertainty = standardUncertainty;
    }


}