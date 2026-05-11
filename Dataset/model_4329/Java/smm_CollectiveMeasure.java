





import java.util.List;
import java.util.ArrayList;

public class smm_CollectiveMeasure extends DimensionalMeasure {

    private String accumulator;





    private smm_Operation smm_operation;


    public smm_CollectiveMeasure(
        String accumulator    ) {
        super(
        );
        this.accumulator = accumulator;
    }


    public String getAccumulator() {
        return accumulator;
    }

    public void setAccumulator(String accumulator) {
        this.accumulator = accumulator;
    }

    public smm_Operation getSmm_operation() {
        return smm_operation;
    }

    public void setSmm_operation(smm_Operation smm_operation) {
        this.smm_operation = smm_operation;
    }

}