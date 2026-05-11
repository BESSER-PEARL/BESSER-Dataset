





import java.util.List;
import java.util.ArrayList;

public class smm_DimensionalMeasurement extends Measurement {

    private float value;





    private List<smm_RankingMeasurementRelationship> smm_rankingmeasurementrelationships;




    private List<smm_Base2MeasurementRelationship> smm_base2measurementrelationships;




    private List<smm_GradeMeasurementRelationship> smm_grademeasurementrelationships;




    private List<smm_BaseNMeasurementRelationship> smm_basenmeasurementrelationships;




    private List<smm_Base1MeasurementRelationship> smm_base1measurementrelationships;


    public smm_DimensionalMeasurement(
        float value    ) {
        super(
        );
        this.value = value;
        this.smm_rankingmeasurementrelationships = new ArrayList<>();
        this.smm_base2measurementrelationships = new ArrayList<>();
        this.smm_grademeasurementrelationships = new ArrayList<>();
        this.smm_basenmeasurementrelationships = new ArrayList<>();
        this.smm_base1measurementrelationships = new ArrayList<>();
    }

    public smm_DimensionalMeasurement(
        float value        ArrayList<smm_RankingMeasurementRelationship> smm_rankingmeasurementrelationships,        ArrayList<smm_Base2MeasurementRelationship> smm_base2measurementrelationships,        ArrayList<smm_GradeMeasurementRelationship> smm_grademeasurementrelationships,        ArrayList<smm_BaseNMeasurementRelationship> smm_basenmeasurementrelationships,        ArrayList<smm_Base1MeasurementRelationship> smm_base1measurementrelationships    ) {
        this.value = value;
        this.smm_rankingmeasurementrelationships = smm_rankingmeasurementrelationships;
        this.smm_base2measurementrelationships = smm_base2measurementrelationships;
        this.smm_grademeasurementrelationships = smm_grademeasurementrelationships;
        this.smm_basenmeasurementrelationships = smm_basenmeasurementrelationships;
        this.smm_base1measurementrelationships = smm_base1measurementrelationships;
    }

    public float getValue() {
        return value;
    }

    public void setValue(float value) {
        this.value = value;
    }

    public List<smm_RankingMeasurementRelationship> getSmm_rankingmeasurementrelationships() {
        return smm_rankingmeasurementrelationships;
    }

    public void addSmm_rankingmeasurementrelationship(Smm_rankingmeasurementrelationship smm_rankingmeasurementrelationship) {
        this.smm_rankingmeasurementrelationships.add(smm_rankingmeasurementrelationship);
    }
    public List<smm_Base2MeasurementRelationship> getSmm_base2measurementrelationships() {
        return smm_base2measurementrelationships;
    }

    public void addSmm_base2measurementrelationship(Smm_base2measurementrelationship smm_base2measurementrelationship) {
        this.smm_base2measurementrelationships.add(smm_base2measurementrelationship);
    }
    public List<smm_GradeMeasurementRelationship> getSmm_grademeasurementrelationships() {
        return smm_grademeasurementrelationships;
    }

    public void addSmm_grademeasurementrelationship(Smm_grademeasurementrelationship smm_grademeasurementrelationship) {
        this.smm_grademeasurementrelationships.add(smm_grademeasurementrelationship);
    }
    public List<smm_BaseNMeasurementRelationship> getSmm_basenmeasurementrelationships() {
        return smm_basenmeasurementrelationships;
    }

    public void addSmm_basenmeasurementrelationship(Smm_basenmeasurementrelationship smm_basenmeasurementrelationship) {
        this.smm_basenmeasurementrelationships.add(smm_basenmeasurementrelationship);
    }
    public List<smm_Base1MeasurementRelationship> getSmm_base1measurementrelationships() {
        return smm_base1measurementrelationships;
    }

    public void addSmm_base1measurementrelationship(Smm_base1measurementrelationship smm_base1measurementrelationship) {
        this.smm_base1measurementrelationships.add(smm_base1measurementrelationship);
    }

}