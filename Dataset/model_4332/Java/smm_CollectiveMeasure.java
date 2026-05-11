





import java.util.List;
import java.util.ArrayList;

public class smm_CollectiveMeasure extends DimensionalMeasure {

    private String accumulator;





    private smm_DimensionalMeasure smm_dimensionalmeasure;


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

    public smm_DimensionalMeasure getSmm_dimensionalmeasure() {
        return smm_dimensionalmeasure;
    }

    public void setSmm_dimensionalmeasure(smm_DimensionalMeasure smm_dimensionalmeasure) {
        this.smm_dimensionalmeasure = smm_dimensionalmeasure;
    }

}