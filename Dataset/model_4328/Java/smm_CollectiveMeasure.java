





import java.util.List;
import java.util.ArrayList;

public class smm_CollectiveMeasure extends DimensionalMeasure {

    private String accumulator;





    private List<smm_BaseNMeasureRelationship> smm_basenmeasurerelationships;




    private smm_Operation smm_operation;


    public smm_CollectiveMeasure(
        String accumulator    ) {
        super(
        );
        this.accumulator = accumulator;
        this.smm_basenmeasurerelationships = new ArrayList<>();
    }

    public smm_CollectiveMeasure(
        String accumulator        ArrayList<smm_BaseNMeasureRelationship> smm_basenmeasurerelationships    ) {
        this.accumulator = accumulator;
        this.smm_basenmeasurerelationships = smm_basenmeasurerelationships;
    }

    public String getAccumulator() {
        return accumulator;
    }

    public void setAccumulator(String accumulator) {
        this.accumulator = accumulator;
    }

    public List<smm_BaseNMeasureRelationship> getSmm_basenmeasurerelationships() {
        return smm_basenmeasurerelationships;
    }

    public void addSmm_basenmeasurerelationship(Smm_basenmeasurerelationship smm_basenmeasurerelationship) {
        this.smm_basenmeasurerelationships.add(smm_basenmeasurerelationship);
    }
    public smm_Operation getSmm_operation() {
        return smm_operation;
    }

    public void setSmm_operation(smm_Operation smm_operation) {
        this.smm_operation = smm_operation;
    }

}