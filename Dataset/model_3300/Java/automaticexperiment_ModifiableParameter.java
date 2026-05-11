





import java.util.List;
import java.util.ArrayList;

public class automaticexperiment_ModifiableParameter  {

    private String targetURI;
    private String featureName;
    private float upperBound;
    private float lowerBound;
    private float initialValue;
    private float step;



    public automaticexperiment_ModifiableParameter(
        String targetURI,        String featureName,        float upperBound,        float lowerBound,        float initialValue,        float step    ) {
        this.targetURI = targetURI;
        this.featureName = featureName;
        this.upperBound = upperBound;
        this.lowerBound = lowerBound;
        this.initialValue = initialValue;
        this.step = step;
    }


    public String getTargeturi() {
        return targetURI;
    }

    public void setTargeturi(String targetURI) {
        this.targetURI = targetURI;
    }
    public String getFeaturename() {
        return featureName;
    }

    public void setFeaturename(String featureName) {
        this.featureName = featureName;
    }
    public float getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(float upperBound) {
        this.upperBound = upperBound;
    }
    public float getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(float lowerBound) {
        this.lowerBound = lowerBound;
    }
    public float getInitialvalue() {
        return initialValue;
    }

    public void setInitialvalue(float initialValue) {
        this.initialValue = initialValue;
    }
    public float getStep() {
        return step;
    }

    public void setStep(float step) {
        this.step = step;
    }


}