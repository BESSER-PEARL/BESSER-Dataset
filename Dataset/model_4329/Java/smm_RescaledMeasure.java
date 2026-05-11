





import java.util.List;
import java.util.ArrayList;

public class smm_RescaledMeasure extends DimensionalMeasure {

    private float multiplier;
    private float offset;
    private String operationFirst;





    private smm_Operation smm_operation;


    public smm_RescaledMeasure(
        float multiplier,        float offset,        String operationFirst    ) {
        super(
        );
        this.multiplier = multiplier;
        this.offset = offset;
        this.operationFirst = operationFirst;
    }


    public float getMultiplier() {
        return multiplier;
    }

    public void setMultiplier(float multiplier) {
        this.multiplier = multiplier;
    }
    public float getOffset() {
        return offset;
    }

    public void setOffset(float offset) {
        this.offset = offset;
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