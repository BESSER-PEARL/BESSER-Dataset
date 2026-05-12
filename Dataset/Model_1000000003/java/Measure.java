





import java.util.List;
import java.util.ArrayList;

public class Measure  {

    private String error;
    private float uncertainty;
    private String unit;
    private String value;





    private Observation observation;




    private Metric metric;




    private Element element;


    public Measure(
        String error,        float uncertainty,        String unit,        String value    ) {
        this.error = error;
        this.uncertainty = uncertainty;
        this.unit = unit;
        this.value = value;
    }


    public String getError() {
        return error;
    }

    public void setError(String error) {
        this.error = error;
    }
    public float getUncertainty() {
        return uncertainty;
    }

    public void setUncertainty(float uncertainty) {
        this.uncertainty = uncertainty;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public Observation getObservation() {
        return observation;
    }

    public void setObservation(Observation observation) {
        this.observation = observation;
    }
    public Metric getMetric() {
        return metric;
    }

    public void setMetric(Metric metric) {
        this.metric = metric;
    }
    public Element getElement() {
        return element;
    }

    public void setElement(Element element) {
        this.element = element;
    }

}