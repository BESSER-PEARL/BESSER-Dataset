





import java.util.List;
import java.util.ArrayList;

public class model_ConversionFactor  {

    private float offset;
    private float multiplicator;





    private model_Unit model_unit;




    private model_Unit model_unit;


    public model_ConversionFactor(
        float offset,        float multiplicator    ) {
        this.offset = offset;
        this.multiplicator = multiplicator;
    }


    public float getOffset() {
        return offset;
    }

    public void setOffset(float offset) {
        this.offset = offset;
    }
    public float getMultiplicator() {
        return multiplicator;
    }

    public void setMultiplicator(float multiplicator) {
        this.multiplicator = multiplicator;
    }

    public model_Unit getModel_unit() {
        return model_unit;
    }

    public void setModel_unit(model_Unit model_unit) {
        this.model_unit = model_unit;
    }
    public model_Unit getModel_unit() {
        return model_unit;
    }

    public void setModel_unit(model_Unit model_unit) {
        this.model_unit = model_unit;
    }

}