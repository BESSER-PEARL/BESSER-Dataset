





import java.util.List;
import java.util.ArrayList;

public class smm_CollectiveMeasure extends DimensionalMeasure {

    private String accumulator;





    private smm_BaseMeasureRelationship smm_basemeasurerelationship;




    private List<smm_BaseMeasureRelationship> smm_basemeasurerelationships;


    public smm_CollectiveMeasure(
        String accumulator    ) {
        super(
        );
        this.accumulator = accumulator;
        this.smm_basemeasurerelationships = new ArrayList<>();
    }

    public smm_CollectiveMeasure(
        String accumulator        ArrayList<smm_BaseMeasureRelationship> smm_basemeasurerelationships    ) {
        this.accumulator = accumulator;
        this.smm_basemeasurerelationships = smm_basemeasurerelationships;
    }

    public String getAccumulator() {
        return accumulator;
    }

    public void setAccumulator(String accumulator) {
        this.accumulator = accumulator;
    }

    public smm_BaseMeasureRelationship getSmm_basemeasurerelationship() {
        return smm_basemeasurerelationship;
    }

    public void setSmm_basemeasurerelationship(smm_BaseMeasureRelationship smm_basemeasurerelationship) {
        this.smm_basemeasurerelationship = smm_basemeasurerelationship;
    }
    public List<smm_BaseMeasureRelationship> getSmm_basemeasurerelationships() {
        return smm_basemeasurerelationships;
    }

    public void addSmm_basemeasurerelationship(Smm_basemeasurerelationship smm_basemeasurerelationship) {
        this.smm_basemeasurerelationships.add(smm_basemeasurerelationship);
    }

}