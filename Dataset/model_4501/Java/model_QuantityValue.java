





import java.util.List;
import java.util.ArrayList;

public class model_QuantityValue  {

    private float value;





    private model_MeasurementUncertainty model_measurementuncertainty;




    private model_Quantity model_quantity;


    public model_QuantityValue(
        float value    ) {
        this.value = value;
    }


    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public model_MeasurementUncertainty getModel_measurementuncertainty() {
        return model_measurementuncertainty;
    }

    public void setModel_measurementuncertainty(model_MeasurementUncertainty model_measurementuncertainty) {
        this.model_measurementuncertainty = model_measurementuncertainty;
    }
    public model_Quantity getModel_quantity() {
        return model_quantity;
    }

    public void setModel_quantity(model_Quantity model_quantity) {
        this.model_quantity = model_quantity;
    }

}