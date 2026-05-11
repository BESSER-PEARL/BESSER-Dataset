





import java.util.List;
import java.util.ArrayList;

public class smm_Measure extends AbstractMeasureElement {

    private String customScale;
    private String measureLabelFormat;
    private String scale;
    private String visible;
    private String source;
    private String measurementLabelFormat;





    private smm_Scope smm_scope;




    private List<smm_MeasureRelationship> smm_measurerelationships;




    private smm_Operation smm_operation;




    private smm_ObservedMeasure smm_observedmeasure;




    private smm_Characteristic smm_characteristic;




    private smm_MeasureCategory smm_measurecategory;




    private List<smm_MeasureCategory> smm_measurecategorys;




    private List<smm_MeasureRelationship> smm_measurerelationships;




    private List<smm_MeasureRelationship> smm_measurerelationships;


    public smm_Measure(
        String customScale,        String measureLabelFormat,        String scale,        String visible,        String source,        String measurementLabelFormat    ) {
        super(
        );
        this.customScale = customScale;
        this.measureLabelFormat = measureLabelFormat;
        this.scale = scale;
        this.visible = visible;
        this.source = source;
        this.measurementLabelFormat = measurementLabelFormat;
        this.smm_measurerelationships = new ArrayList<>();
        this.smm_measurecategorys = new ArrayList<>();
        this.smm_measurerelationships = new ArrayList<>();
        this.smm_measurerelationships = new ArrayList<>();
    }

    public smm_Measure(
        String customScale,        String measureLabelFormat,        String scale,        String visible,        String source,        String measurementLabelFormat        ArrayList<smm_MeasureRelationship> smm_measurerelationships,        ArrayList<smm_MeasureCategory> smm_measurecategorys,        ArrayList<smm_MeasureRelationship> smm_measurerelationships,        ArrayList<smm_MeasureRelationship> smm_measurerelationships    ) {
        this.customScale = customScale;
        this.measureLabelFormat = measureLabelFormat;
        this.scale = scale;
        this.visible = visible;
        this.source = source;
        this.measurementLabelFormat = measurementLabelFormat;
        this.smm_measurerelationships = smm_measurerelationships;
        this.smm_measurecategorys = smm_measurecategorys;
        this.smm_measurerelationships = smm_measurerelationships;
        this.smm_measurerelationships = smm_measurerelationships;
    }

    public String getCustomscale() {
        return customScale;
    }

    public void setCustomscale(String customScale) {
        this.customScale = customScale;
    }
    public String getMeasurelabelformat() {
        return measureLabelFormat;
    }

    public void setMeasurelabelformat(String measureLabelFormat) {
        this.measureLabelFormat = measureLabelFormat;
    }
    public String getScale() {
        return scale;
    }

    public void setScale(String scale) {
        this.scale = scale;
    }
    public String getVisible() {
        return visible;
    }

    public void setVisible(String visible) {
        this.visible = visible;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getMeasurementlabelformat() {
        return measurementLabelFormat;
    }

    public void setMeasurementlabelformat(String measurementLabelFormat) {
        this.measurementLabelFormat = measurementLabelFormat;
    }

    public smm_Scope getSmm_scope() {
        return smm_scope;
    }

    public void setSmm_scope(smm_Scope smm_scope) {
        this.smm_scope = smm_scope;
    }
    public List<smm_MeasureRelationship> getSmm_measurerelationships() {
        return smm_measurerelationships;
    }

    public void addSmm_measurerelationship(Smm_measurerelationship smm_measurerelationship) {
        this.smm_measurerelationships.add(smm_measurerelationship);
    }
    public smm_Operation getSmm_operation() {
        return smm_operation;
    }

    public void setSmm_operation(smm_Operation smm_operation) {
        this.smm_operation = smm_operation;
    }
    public smm_ObservedMeasure getSmm_observedmeasure() {
        return smm_observedmeasure;
    }

    public void setSmm_observedmeasure(smm_ObservedMeasure smm_observedmeasure) {
        this.smm_observedmeasure = smm_observedmeasure;
    }
    public smm_Characteristic getSmm_characteristic() {
        return smm_characteristic;
    }

    public void setSmm_characteristic(smm_Characteristic smm_characteristic) {
        this.smm_characteristic = smm_characteristic;
    }
    public smm_MeasureCategory getSmm_measurecategory() {
        return smm_measurecategory;
    }

    public void setSmm_measurecategory(smm_MeasureCategory smm_measurecategory) {
        this.smm_measurecategory = smm_measurecategory;
    }
    public List<smm_MeasureCategory> getSmm_measurecategorys() {
        return smm_measurecategorys;
    }

    public void addSmm_measurecategory(Smm_measurecategory smm_measurecategory) {
        this.smm_measurecategorys.add(smm_measurecategory);
    }
    public List<smm_MeasureRelationship> getSmm_measurerelationships() {
        return smm_measurerelationships;
    }

    public void addSmm_measurerelationship(Smm_measurerelationship smm_measurerelationship) {
        this.smm_measurerelationships.add(smm_measurerelationship);
    }
    public List<smm_MeasureRelationship> getSmm_measurerelationships() {
        return smm_measurerelationships;
    }

    public void addSmm_measurerelationship(Smm_measurerelationship smm_measurerelationship) {
        this.smm_measurerelationships.add(smm_measurerelationship);
    }

}