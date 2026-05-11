





import java.util.List;
import java.util.ArrayList;

public class smm_DimensionalMeasure extends Measure {

    private String unit;





    private smm_Base1MeasureRelationship smm_base1measurerelationship;




    private smm_BaseMeasureRelationship smm_basemeasurerelationship;




    private List<smm_Base2MeasureRelationship> smm_base2measurerelationships;




    private smm_Base2MeasureRelationship smm_base2measurerelationship;




    private smm_RescaleMeasureRelationship smm_rescalemeasurerelationship;




    private List<smm_RankingMeasureRelationship> smm_rankingmeasurerelationships;




    private List<smm_BaseMeasureRelationship> smm_basemeasurerelationships;




    private List<smm_Base1MeasureRelationship> smm_base1measurerelationships;




    private smm_RescaleMeasureRelationship smm_rescalemeasurerelationship;




    private smm_RankingMeasureRelationship smm_rankingmeasurerelationship;


    public smm_DimensionalMeasure(
        String unit    ) {
        super(
        );
        this.unit = unit;
        this.smm_base2measurerelationships = new ArrayList<>();
        this.smm_rankingmeasurerelationships = new ArrayList<>();
        this.smm_basemeasurerelationships = new ArrayList<>();
        this.smm_base1measurerelationships = new ArrayList<>();
    }

    public smm_DimensionalMeasure(
        String unit        ArrayList<smm_Base2MeasureRelationship> smm_base2measurerelationships,        ArrayList<smm_RankingMeasureRelationship> smm_rankingmeasurerelationships,        ArrayList<smm_BaseMeasureRelationship> smm_basemeasurerelationships,        ArrayList<smm_Base1MeasureRelationship> smm_base1measurerelationships    ) {
        this.unit = unit;
        this.smm_base2measurerelationships = smm_base2measurerelationships;
        this.smm_rankingmeasurerelationships = smm_rankingmeasurerelationships;
        this.smm_basemeasurerelationships = smm_basemeasurerelationships;
        this.smm_base1measurerelationships = smm_base1measurerelationships;
    }

    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }

    public smm_Base1MeasureRelationship getSmm_base1measurerelationship() {
        return smm_base1measurerelationship;
    }

    public void setSmm_base1measurerelationship(smm_Base1MeasureRelationship smm_base1measurerelationship) {
        this.smm_base1measurerelationship = smm_base1measurerelationship;
    }
    public smm_BaseMeasureRelationship getSmm_basemeasurerelationship() {
        return smm_basemeasurerelationship;
    }

    public void setSmm_basemeasurerelationship(smm_BaseMeasureRelationship smm_basemeasurerelationship) {
        this.smm_basemeasurerelationship = smm_basemeasurerelationship;
    }
    public List<smm_Base2MeasureRelationship> getSmm_base2measurerelationships() {
        return smm_base2measurerelationships;
    }

    public void addSmm_base2measurerelationship(Smm_base2measurerelationship smm_base2measurerelationship) {
        this.smm_base2measurerelationships.add(smm_base2measurerelationship);
    }
    public smm_Base2MeasureRelationship getSmm_base2measurerelationship() {
        return smm_base2measurerelationship;
    }

    public void setSmm_base2measurerelationship(smm_Base2MeasureRelationship smm_base2measurerelationship) {
        this.smm_base2measurerelationship = smm_base2measurerelationship;
    }
    public smm_RescaleMeasureRelationship getSmm_rescalemeasurerelationship() {
        return smm_rescalemeasurerelationship;
    }

    public void setSmm_rescalemeasurerelationship(smm_RescaleMeasureRelationship smm_rescalemeasurerelationship) {
        this.smm_rescalemeasurerelationship = smm_rescalemeasurerelationship;
    }
    public List<smm_RankingMeasureRelationship> getSmm_rankingmeasurerelationships() {
        return smm_rankingmeasurerelationships;
    }

    public void addSmm_rankingmeasurerelationship(Smm_rankingmeasurerelationship smm_rankingmeasurerelationship) {
        this.smm_rankingmeasurerelationships.add(smm_rankingmeasurerelationship);
    }
    public List<smm_BaseMeasureRelationship> getSmm_basemeasurerelationships() {
        return smm_basemeasurerelationships;
    }

    public void addSmm_basemeasurerelationship(Smm_basemeasurerelationship smm_basemeasurerelationship) {
        this.smm_basemeasurerelationships.add(smm_basemeasurerelationship);
    }
    public List<smm_Base1MeasureRelationship> getSmm_base1measurerelationships() {
        return smm_base1measurerelationships;
    }

    public void addSmm_base1measurerelationship(Smm_base1measurerelationship smm_base1measurerelationship) {
        this.smm_base1measurerelationships.add(smm_base1measurerelationship);
    }
    public smm_RescaleMeasureRelationship getSmm_rescalemeasurerelationship() {
        return smm_rescalemeasurerelationship;
    }

    public void setSmm_rescalemeasurerelationship(smm_RescaleMeasureRelationship smm_rescalemeasurerelationship) {
        this.smm_rescalemeasurerelationship = smm_rescalemeasurerelationship;
    }
    public smm_RankingMeasureRelationship getSmm_rankingmeasurerelationship() {
        return smm_rankingmeasurerelationship;
    }

    public void setSmm_rankingmeasurerelationship(smm_RankingMeasureRelationship smm_rankingmeasurerelationship) {
        this.smm_rankingmeasurerelationship = smm_rankingmeasurerelationship;
    }

}