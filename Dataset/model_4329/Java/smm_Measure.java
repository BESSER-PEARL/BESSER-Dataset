





import java.util.List;
import java.util.ArrayList;

public class smm_Measure extends AbstractMeasureElement {

    private String customScale;
    private String source;
    private String measureLabelFormat;
    private String scale;
    private String measurementLabelFormat;
    private String visible;





    private List<smm_MeasureRelationship> smm_measurerelationships;




    private smm_ObservedMeasure smm_observedmeasure;




    private List<smm_MeasureRelationship> smm_measurerelationships;




    private List<smm_MeasureRelationship> smm_measurerelationships;




    private smm_Characteristic smm_characteristic;


    public smm_Measure(
        String customScale,        String source,        String measureLabelFormat,        String scale,        String measurementLabelFormat,        String visible    ) {
        super(
        );
        this.customScale = customScale;
        this.source = source;
        this.measureLabelFormat = measureLabelFormat;
        this.scale = scale;
        this.measurementLabelFormat = measurementLabelFormat;
        this.visible = visible;
        this.smm_measurerelationships = new ArrayList<>();
        this.smm_measurerelationships = new ArrayList<>();
        this.smm_measurerelationships = new ArrayList<>();
    }

    public smm_Measure(
        String customScale,        String source,        String measureLabelFormat,        String scale,        String measurementLabelFormat,        String visible        ArrayList<smm_MeasureRelationship> smm_measurerelationships,        ArrayList<smm_MeasureRelationship> smm_measurerelationships,        ArrayList<smm_MeasureRelationship> smm_measurerelationships    ) {
        this.customScale = customScale;
        this.source = source;
        this.measureLabelFormat = measureLabelFormat;
        this.scale = scale;
        this.measurementLabelFormat = measurementLabelFormat;
        this.visible = visible;
        this.smm_measurerelationships = smm_measurerelationships;
        this.smm_measurerelationships = smm_measurerelationships;
        this.smm_measurerelationships = smm_measurerelationships;
    }

    public String getCustomscale() {
        return customScale;
    }

    public void setCustomscale(String customScale) {
        this.customScale = customScale;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
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
    public String getMeasurementlabelformat() {
        return measurementLabelFormat;
    }

    public void setMeasurementlabelformat(String measurementLabelFormat) {
        this.measurementLabelFormat = measurementLabelFormat;
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
    public smm_ObservedMeasure getSmm_observedmeasure() {
        return smm_observedmeasure;
    }

    public void setSmm_observedmeasure(smm_ObservedMeasure smm_observedmeasure) {
        this.smm_observedmeasure = smm_observedmeasure;
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
    public smm_Characteristic getSmm_characteristic() {
        return smm_characteristic;
    }

    public void setSmm_characteristic(smm_Characteristic smm_characteristic) {
        this.smm_characteristic = smm_characteristic;
    }

}