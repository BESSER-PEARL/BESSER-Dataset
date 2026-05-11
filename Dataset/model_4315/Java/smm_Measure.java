





import java.util.List;
import java.util.ArrayList;

public class smm_Measure extends AbstractMeasureElement {

    private String measurementLabelFormat;
    private String measureLabelFormat;
    private String visible;





    private List<smm_MeasureRelationship> smm_measurerelationships;




    private smm_RefinementMeasureRelationship smm_refinementmeasurerelationship;




    private smm_RecursiveMeasureRelationship smm_recursivemeasurerelationship;




    private smm_MeasureCategory smm_measurecategory;




    private smm_RecursiveMeasureRelationship smm_recursivemeasurerelationship;




    private smm_ObservedMeasure smm_observedmeasure;




    private smm_EquivalentMeasureRelationship smm_equivalentmeasurerelationship;




    private smm_EquivalentMeasureRelationship smm_equivalentmeasurerelationship;




    private List<smm_EquivalentMeasureRelationship> smm_equivalentmeasurerelationships;




    private smm_RecursiveMeasureRelationship smm_recursivemeasurerelationship;




    private List<smm_RefinementMeasureRelationship> smm_refinementmeasurerelationships;




    private List<smm_MeasureRelationship> smm_measurerelationships;




    private smm_RefinementMeasureRelationship smm_refinementmeasurerelationship;




    private smm_RecursiveMeasureRelationship smm_recursivemeasurerelationship;




    private List<smm_MeasureRelationship> smm_measurerelationships;




    private List<smm_EquivalentMeasureRelationship> smm_equivalentmeasurerelationships;




    private List<smm_MeasureCategory> smm_measurecategorys;




    private List<smm_RefinementMeasureRelationship> smm_refinementmeasurerelationships;




    private smm_Characteristic smm_characteristic;


    public smm_Measure(
        String measurementLabelFormat,        String measureLabelFormat,        String visible    ) {
        super(
        );
        this.measurementLabelFormat = measurementLabelFormat;
        this.measureLabelFormat = measureLabelFormat;
        this.visible = visible;
        this.smm_measurerelationships = new ArrayList<>();
        this.smm_equivalentmeasurerelationships = new ArrayList<>();
        this.smm_refinementmeasurerelationships = new ArrayList<>();
        this.smm_measurerelationships = new ArrayList<>();
        this.smm_measurerelationships = new ArrayList<>();
        this.smm_equivalentmeasurerelationships = new ArrayList<>();
        this.smm_measurecategorys = new ArrayList<>();
        this.smm_refinementmeasurerelationships = new ArrayList<>();
    }

    public smm_Measure(
        String measurementLabelFormat,        String measureLabelFormat,        String visible        ArrayList<smm_MeasureRelationship> smm_measurerelationships,        ArrayList<smm_EquivalentMeasureRelationship> smm_equivalentmeasurerelationships,        ArrayList<smm_RefinementMeasureRelationship> smm_refinementmeasurerelationships,        ArrayList<smm_MeasureRelationship> smm_measurerelationships,        ArrayList<smm_MeasureRelationship> smm_measurerelationships,        ArrayList<smm_EquivalentMeasureRelationship> smm_equivalentmeasurerelationships,        ArrayList<smm_MeasureCategory> smm_measurecategorys,        ArrayList<smm_RefinementMeasureRelationship> smm_refinementmeasurerelationships    ) {
        this.measurementLabelFormat = measurementLabelFormat;
        this.measureLabelFormat = measureLabelFormat;
        this.visible = visible;
        this.smm_measurerelationships = smm_measurerelationships;
        this.smm_equivalentmeasurerelationships = smm_equivalentmeasurerelationships;
        this.smm_refinementmeasurerelationships = smm_refinementmeasurerelationships;
        this.smm_measurerelationships = smm_measurerelationships;
        this.smm_measurerelationships = smm_measurerelationships;
        this.smm_equivalentmeasurerelationships = smm_equivalentmeasurerelationships;
        this.smm_measurecategorys = smm_measurecategorys;
        this.smm_refinementmeasurerelationships = smm_refinementmeasurerelationships;
    }

    public String getMeasurementlabelformat() {
        return measurementLabelFormat;
    }

    public void setMeasurementlabelformat(String measurementLabelFormat) {
        this.measurementLabelFormat = measurementLabelFormat;
    }
    public String getMeasurelabelformat() {
        return measureLabelFormat;
    }

    public void setMeasurelabelformat(String measureLabelFormat) {
        this.measureLabelFormat = measureLabelFormat;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }

    public List<smm_MeasureRelationship> getSmm_measurerelationships() {
        return smm_measurerelationships;
    }

    public void addSmm_measurerelationship(Smm_measurerelationship smm_measurerelationship) {
        this.smm_measurerelationships.add(smm_measurerelationship);
    }
    public smm_RefinementMeasureRelationship getSmm_refinementmeasurerelationship() {
        return smm_refinementmeasurerelationship;
    }

    public void setSmm_refinementmeasurerelationship(smm_RefinementMeasureRelationship smm_refinementmeasurerelationship) {
        this.smm_refinementmeasurerelationship = smm_refinementmeasurerelationship;
    }
    public smm_RecursiveMeasureRelationship getSmm_recursivemeasurerelationship() {
        return smm_recursivemeasurerelationship;
    }

    public void setSmm_recursivemeasurerelationship(smm_RecursiveMeasureRelationship smm_recursivemeasurerelationship) {
        this.smm_recursivemeasurerelationship = smm_recursivemeasurerelationship;
    }
    public smm_MeasureCategory getSmm_measurecategory() {
        return smm_measurecategory;
    }

    public void setSmm_measurecategory(smm_MeasureCategory smm_measurecategory) {
        this.smm_measurecategory = smm_measurecategory;
    }
    public smm_RecursiveMeasureRelationship getSmm_recursivemeasurerelationship() {
        return smm_recursivemeasurerelationship;
    }

    public void setSmm_recursivemeasurerelationship(smm_RecursiveMeasureRelationship smm_recursivemeasurerelationship) {
        this.smm_recursivemeasurerelationship = smm_recursivemeasurerelationship;
    }
    public smm_ObservedMeasure getSmm_observedmeasure() {
        return smm_observedmeasure;
    }

    public void setSmm_observedmeasure(smm_ObservedMeasure smm_observedmeasure) {
        this.smm_observedmeasure = smm_observedmeasure;
    }
    public smm_EquivalentMeasureRelationship getSmm_equivalentmeasurerelationship() {
        return smm_equivalentmeasurerelationship;
    }

    public void setSmm_equivalentmeasurerelationship(smm_EquivalentMeasureRelationship smm_equivalentmeasurerelationship) {
        this.smm_equivalentmeasurerelationship = smm_equivalentmeasurerelationship;
    }
    public smm_EquivalentMeasureRelationship getSmm_equivalentmeasurerelationship() {
        return smm_equivalentmeasurerelationship;
    }

    public void setSmm_equivalentmeasurerelationship(smm_EquivalentMeasureRelationship smm_equivalentmeasurerelationship) {
        this.smm_equivalentmeasurerelationship = smm_equivalentmeasurerelationship;
    }
    public List<smm_EquivalentMeasureRelationship> getSmm_equivalentmeasurerelationships() {
        return smm_equivalentmeasurerelationships;
    }

    public void addSmm_equivalentmeasurerelationship(Smm_equivalentmeasurerelationship smm_equivalentmeasurerelationship) {
        this.smm_equivalentmeasurerelationships.add(smm_equivalentmeasurerelationship);
    }
    public smm_RecursiveMeasureRelationship getSmm_recursivemeasurerelationship() {
        return smm_recursivemeasurerelationship;
    }

    public void setSmm_recursivemeasurerelationship(smm_RecursiveMeasureRelationship smm_recursivemeasurerelationship) {
        this.smm_recursivemeasurerelationship = smm_recursivemeasurerelationship;
    }
    public List<smm_RefinementMeasureRelationship> getSmm_refinementmeasurerelationships() {
        return smm_refinementmeasurerelationships;
    }

    public void addSmm_refinementmeasurerelationship(Smm_refinementmeasurerelationship smm_refinementmeasurerelationship) {
        this.smm_refinementmeasurerelationships.add(smm_refinementmeasurerelationship);
    }
    public List<smm_MeasureRelationship> getSmm_measurerelationships() {
        return smm_measurerelationships;
    }

    public void addSmm_measurerelationship(Smm_measurerelationship smm_measurerelationship) {
        this.smm_measurerelationships.add(smm_measurerelationship);
    }
    public smm_RefinementMeasureRelationship getSmm_refinementmeasurerelationship() {
        return smm_refinementmeasurerelationship;
    }

    public void setSmm_refinementmeasurerelationship(smm_RefinementMeasureRelationship smm_refinementmeasurerelationship) {
        this.smm_refinementmeasurerelationship = smm_refinementmeasurerelationship;
    }
    public smm_RecursiveMeasureRelationship getSmm_recursivemeasurerelationship() {
        return smm_recursivemeasurerelationship;
    }

    public void setSmm_recursivemeasurerelationship(smm_RecursiveMeasureRelationship smm_recursivemeasurerelationship) {
        this.smm_recursivemeasurerelationship = smm_recursivemeasurerelationship;
    }
    public List<smm_MeasureRelationship> getSmm_measurerelationships() {
        return smm_measurerelationships;
    }

    public void addSmm_measurerelationship(Smm_measurerelationship smm_measurerelationship) {
        this.smm_measurerelationships.add(smm_measurerelationship);
    }
    public List<smm_EquivalentMeasureRelationship> getSmm_equivalentmeasurerelationships() {
        return smm_equivalentmeasurerelationships;
    }

    public void addSmm_equivalentmeasurerelationship(Smm_equivalentmeasurerelationship smm_equivalentmeasurerelationship) {
        this.smm_equivalentmeasurerelationships.add(smm_equivalentmeasurerelationship);
    }
    public List<smm_MeasureCategory> getSmm_measurecategorys() {
        return smm_measurecategorys;
    }

    public void addSmm_measurecategory(Smm_measurecategory smm_measurecategory) {
        this.smm_measurecategorys.add(smm_measurecategory);
    }
    public List<smm_RefinementMeasureRelationship> getSmm_refinementmeasurerelationships() {
        return smm_refinementmeasurerelationships;
    }

    public void addSmm_refinementmeasurerelationship(Smm_refinementmeasurerelationship smm_refinementmeasurerelationship) {
        this.smm_refinementmeasurerelationships.add(smm_refinementmeasurerelationship);
    }
    public smm_Characteristic getSmm_characteristic() {
        return smm_characteristic;
    }

    public void setSmm_characteristic(smm_Characteristic smm_characteristic) {
        this.smm_characteristic = smm_characteristic;
    }

}