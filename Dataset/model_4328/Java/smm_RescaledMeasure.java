





import java.util.List;
import java.util.ArrayList;

public class smm_RescaledMeasure extends DimensionalMeasure {

    private float offset;
    private float multiplier;
    private String operationFirst;





    private smm_Operation smm_operation;


    public smm_RescaledMeasure(
        float offset,        float multiplier,        String operationFirst    ) {
        super(
        );
        this.offset = offset;
        this.multiplier = multiplier;
        this.operationFirst = operationFirst;
    }


    public float getOffset() {
        return offset;
    }

    public void setOffset(float offset) {
        this.offset = offset;
    }
    public float getMultiplier() {
        return multiplier;
    }

    public void setMultiplier(float multiplier) {
        this.multiplier = multiplier;
    }
    public String getOperationfirst() {
        return operationFirst;
    }

    public void setOperationfirst(String operationFirst) {
        this.operationFirst = operationFirst;
    }

    public smm_Operation getSmm_operation() {
        return smm_operation;
    }

    public void setSmm_operation(smm_Operation smm_operation) {
        this.smm_operation = smm_operation;
    }

}