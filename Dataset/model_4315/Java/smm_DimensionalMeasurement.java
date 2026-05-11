





import java.util.List;
import java.util.ArrayList;

public class smm_DimensionalMeasurement extends Measurement {

    private String value;





    private smm_Base2MeasurementRelationship smm_base2measurementrelationship;




    private smm_RankingMeasurementRelationship smm_rankingmeasurementrelationship;




    private List<smm_BaseMeasurementRelationship> smm_basemeasurementrelationships;




    private List<smm_Base1MeasurementRelationship> smm_base1measurementrelationships;




    private smm_RescaleMeasurementRelationship smm_rescalemeasurementrelationship;




    private List<smm_Base2MeasurementRelationship> smm_base2measurementrelationships;




    private smm_BaseMeasurementRelationship smm_basemeasurementrelationship;




    private List<smm_RankingMeasurementRelationship> smm_rankingmeasurementrelationships;




    private List<smm_RescaleMeasurementRelationship> smm_rescalemeasurementrelationships;




    private smm_Base1MeasurementRelationship smm_base1measurementrelationship;


    public smm_DimensionalMeasurement(
        String value    ) {
        super(
        );
        this.value = value;
        this.smm_basemeasurementrelationships = new ArrayList<>();
        this.smm_base1measurementrelationships = new ArrayList<>();
        this.smm_base2measurementrelationships = new ArrayList<>();
        this.smm_rankingmeasurementrelationships = new ArrayList<>();
        this.smm_rescalemeasurementrelationships = new ArrayList<>();
    }

    public smm_DimensionalMeasurement(
        String value        ArrayList<smm_BaseMeasurementRelationship> smm_basemeasurementrelationships,        ArrayList<smm_Base1MeasurementRelationship> smm_base1measurementrelationships,        ArrayList<smm_Base2MeasurementRelationship> smm_base2measurementrelationships,        ArrayList<smm_RankingMeasurementRelationship> smm_rankingmeasurementrelationships,        ArrayList<smm_RescaleMeasurementRelationship> smm_rescalemeasurementrelationships    ) {
        this.value = value;
        this.smm_basemeasurementrelationships = smm_basemeasurementrelationships;
        this.smm_base1measurementrelationships = smm_base1measurementrelationships;
        this.smm_base2measurementrelationships = smm_base2measurementrelationships;
        this.smm_rankingmeasurementrelationships = smm_rankingmeasurementrelationships;
        this.smm_rescalemeasurementrelationships = smm_rescalemeasurementrelationships;
    }

    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public smm_Base2MeasurementRelationship getSmm_base2measurementrelationship() {
        return smm_base2measurementrelationship;
    }

    public void setSmm_base2measurementrelationship(smm_Base2MeasurementRelationship smm_base2measurementrelationship) {
        this.smm_base2measurementrelationship = smm_base2measurementrelationship;
    }
    public smm_RankingMeasurementRelationship getSmm_rankingmeasurementrelationship() {
        return smm_rankingmeasurementrelationship;
    }

    public void setSmm_rankingmeasurementrelationship(smm_RankingMeasurementRelationship smm_rankingmeasurementrelationship) {
        this.smm_rankingmeasurementrelationship = smm_rankingmeasurementrelationship;
    }
    public List<smm_BaseMeasurementRelationship> getSmm_basemeasurementrelationships() {
        return smm_basemeasurementrelationships;
    }

    public void addSmm_basemeasurementrelationship(Smm_basemeasurementrelationship smm_basemeasurementrelationship) {
        this.smm_basemeasurementrelationships.add(smm_basemeasurementrelationship);
    }
    public List<smm_Base1MeasurementRelationship> getSmm_base1measurementrelationships() {
        return smm_base1measurementrelationships;
    }

    public void addSmm_base1measurementrelationship(Smm_base1measurementrelationship smm_base1measurementrelationship) {
        this.smm_base1measurementrelationships.add(smm_base1measurementrelationship);
    }
    public smm_RescaleMeasurementRelationship getSmm_rescalemeasurementrelationship() {
        return smm_rescalemeasurementrelationship;
    }

    public void setSmm_rescalemeasurementrelationship(smm_RescaleMeasurementRelationship smm_rescalemeasurementrelationship) {
        this.smm_rescalemeasurementrelationship = smm_rescalemeasurementrelationship;
    }
    public List<smm_Base2MeasurementRelationship> getSmm_base2measurementrelationships() {
        return smm_base2measurementrelationships;
    }

    public void addSmm_base2measurementrelationship(Smm_base2measurementrelationship smm_base2measurementrelationship) {
        this.smm_base2measurementrelationships.add(smm_base2measurementrelationship);
    }
    public smm_BaseMeasurementRelationship getSmm_basemeasurementrelationship() {
        return smm_basemeasurementrelationship;
    }

    public void setSmm_basemeasurementrelationship(smm_BaseMeasurementRelationship smm_basemeasurementrelationship) {
        this.smm_basemeasurementrelationship = smm_basemeasurementrelationship;
    }
    public List<smm_RankingMeasurementRelationship> getSmm_rankingmeasurementrelationships() {
        return smm_rankingmeasurementrelationships;
    }

    public void addSmm_rankingmeasurementrelationship(Smm_rankingmeasurementrelationship smm_rankingmeasurementrelationship) {
        this.smm_rankingmeasurementrelationships.add(smm_rankingmeasurementrelationship);
    }
    public List<smm_RescaleMeasurementRelationship> getSmm_rescalemeasurementrelationships() {
        return smm_rescalemeasurementrelationships;
    }

    public void addSmm_rescalemeasurementrelationship(Smm_rescalemeasurementrelationship smm_rescalemeasurementrelationship) {
        this.smm_rescalemeasurementrelationships.add(smm_rescalemeasurementrelationship);
    }
    public smm_Base1MeasurementRelationship getSmm_base1measurementrelationship() {
        return smm_base1measurementrelationship;
    }

    public void setSmm_base1measurementrelationship(smm_Base1MeasurementRelationship smm_base1measurementrelationship) {
        this.smm_base1measurementrelationship = smm_base1measurementrelationship;
    }

}