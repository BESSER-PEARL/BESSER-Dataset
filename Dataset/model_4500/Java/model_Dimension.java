





import java.util.List;
import java.util.ArrayList;

public class model_Dimension  {

    private float exponent;





    private model_Unit model_unit;


    public model_Dimension(
        float exponent    ) {
        this.exponent = exponent;
    }


    public float getExponent() {
        return exponent;
    }

    public void setExponent(float exponent) {
        this.exponent = exponent;
    }

    public model_Unit getModel_unit() {
        return model_unit;
    }

    public void setModel_unit(model_Unit model_unit) {
        this.model_unit = model_unit;
    }

}