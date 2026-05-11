





import java.util.List;
import java.util.ArrayList;

public class smm_RescaledMeasure extends DimensionalMeasure {

    private String formula;





    private List<smm_RescaleMeasureRelationship> smm_rescalemeasurerelationships;




    private smm_RescaleMeasureRelationship smm_rescalemeasurerelationship;


    public smm_RescaledMeasure(
        String formula    ) {
        super(
        );
        this.formula = formula;
        this.smm_rescalemeasurerelationships = new ArrayList<>();
    }

    public smm_RescaledMeasure(
        String formula        ArrayList<smm_RescaleMeasureRelationship> smm_rescalemeasurerelationships    ) {
        this.formula = formula;
        this.smm_rescalemeasurerelationships = smm_rescalemeasurerelationships;
    }

    public String getFormula() {
        return formula;
    }

    public void setFormula(String formula) {
        this.formula = formula;
    }

    public List<smm_RescaleMeasureRelationship> getSmm_rescalemeasurerelationships() {
        return smm_rescalemeasurerelationships;
    }

    public void addSmm_rescalemeasurerelationship(Smm_rescalemeasurerelationship smm_rescalemeasurerelationship) {
        this.smm_rescalemeasurerelationships.add(smm_rescalemeasurerelationship);
    }
    public smm_RescaleMeasureRelationship getSmm_rescalemeasurerelationship() {
        return smm_rescalemeasurerelationship;
    }

    public void setSmm_rescalemeasurerelationship(smm_RescaleMeasureRelationship smm_rescalemeasurerelationship) {
        this.smm_rescalemeasurerelationship = smm_rescalemeasurerelationship;
    }

}