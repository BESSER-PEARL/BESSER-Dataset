





import java.util.List;
import java.util.ArrayList;

public class model_MeasurementUncertainty  {

    private float standardUncertainty;





    private model_QuantityValue model_quantityvalue;


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

    public model_QuantityValue getModel_quantityvalue() {
        return model_quantityvalue;
    }

    public void setModel_quantityvalue(model_QuantityValue model_quantityvalue) {
        this.model_quantityvalue = model_quantityvalue;
    }

}