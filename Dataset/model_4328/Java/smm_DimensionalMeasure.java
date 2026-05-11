





import java.util.List;
import java.util.ArrayList;

public class smm_DimensionalMeasure extends Measure {

    private String formula;





    private List<smm_Base2MeasureRelationship> smm_base2measurerelationships;




    private List<smm_Base1MeasureRelationship> smm_base1measurerelationships;




    private List<smm_GradeMeasureRelationship> smm_grademeasurerelationships;




    private smm_UnitOfMeasure smm_unitofmeasure;




    private List<smm_BaseNMeasureRelationship> smm_basenmeasurerelationships;




    private List<smm_RankingMeasureRelationship> smm_rankingmeasurerelationships;


    public smm_DimensionalMeasure(
        String formula    ) {
        super(
        );
        this.formula = formula;
        this.smm_base2measurerelationships = new ArrayList<>();
        this.smm_base1measurerelationships = new ArrayList<>();
        this.smm_grademeasurerelationships = new ArrayList<>();
        this.smm_basenmeasurerelationships = new ArrayList<>();
        this.smm_rankingmeasurerelationships = new ArrayList<>();
    }

    public smm_DimensionalMeasure(
        String formula        ArrayList<smm_Base2MeasureRelationship> smm_base2measurerelationships,        ArrayList<smm_Base1MeasureRelationship> smm_base1measurerelationships,        ArrayList<smm_GradeMeasureRelationship> smm_grademeasurerelationships,        ArrayList<smm_BaseNMeasureRelationship> smm_basenmeasurerelationships,        ArrayList<smm_RankingMeasureRelationship> smm_rankingmeasurerelationships    ) {
        this.formula = formula;
        this.smm_base2measurerelationships = smm_base2measurerelationships;
        this.smm_base1measurerelationships = smm_base1measurerelationships;
        this.smm_grademeasurerelationships = smm_grademeasurerelationships;
        this.smm_basenmeasurerelationships = smm_basenmeasurerelationships;
        this.smm_rankingmeasurerelationships = smm_rankingmeasurerelationships;
    }

    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }

    public List<smm_Base2MeasureRelationship> getSmm_base2measurerelationships() {
        return smm_base2measurerelationships;
    }

    public void addSmm_base2measurerelationship(Smm_base2measurerelationship smm_base2measurerelationship) {
        this.smm_base2measurerelationships.add(smm_base2measurerelationship);
    }
    public List<smm_Base1MeasureRelationship> getSmm_base1measurerelationships() {
        return smm_base1measurerelationships;
    }

    public void addSmm_base1measurerelationship(Smm_base1measurerelationship smm_base1measurerelationship) {
        this.smm_base1measurerelationships.add(smm_base1measurerelationship);
    }
    public List<smm_GradeMeasureRelationship> getSmm_grademeasurerelationships() {
        return smm_grademeasurerelationships;
    }

    public void addSmm_grademeasurerelationship(Smm_grademeasurerelationship smm_grademeasurerelationship) {
        this.smm_grademeasurerelationships.add(smm_grademeasurerelationship);
    }
    public smm_UnitOfMeasure getSmm_unitofmeasure() {
        return smm_unitofmeasure;
    }

    public void setSmm_unitofmeasure(smm_UnitOfMeasure smm_unitofmeasure) {
        this.smm_unitofmeasure = smm_unitofmeasure;
    }
    public List<smm_BaseNMeasureRelationship> getSmm_basenmeasurerelationships() {
        return smm_basenmeasurerelationships;
    }

    public void addSmm_basenmeasurerelationship(Smm_basenmeasurerelationship smm_basenmeasurerelationship) {
        this.smm_basenmeasurerelationships.add(smm_basenmeasurerelationship);
    }
    public List<smm_RankingMeasureRelationship> getSmm_rankingmeasurerelationships() {
        return smm_rankingmeasurerelationships;
    }

    public void addSmm_rankingmeasurerelationship(Smm_rankingmeasurerelationship smm_rankingmeasurerelationship) {
        this.smm_rankingmeasurerelationships.add(smm_rankingmeasurerelationship);
    }

}