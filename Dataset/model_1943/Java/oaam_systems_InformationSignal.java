





import java.util.List;
import java.util.ArrayList;

public class oaam_systems_InformationSignal extends common_OaamBaseElementA, scenario_ModeDependentElementA, systems_ProvidedInformationA, scenario_VariantDependentElementA, systems_RequiredInformationA {

    private float latency;
    private float resolution;
    private String unit;
    private float accuracy;
    private float rate;



    public oaam_systems_InformationSignal(
        float latency,        float resolution,        String unit,        float accuracy,        float rate    ) {
        super(
        );
        this.latency = latency;
        this.resolution = resolution;
        this.unit = unit;
        this.accuracy = accuracy;
        this.rate = rate;
    }


    public float getLatency() {
        return latency;
    }

    public void setLatency(float latency) {
        this.latency = latency;
    }
    public float getResolution() {
        return resolution;
    }

    public void setResolution(float resolution) {
        this.resolution = resolution;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public float getAccuracy() {
        return accuracy;
    }

    public void setAccuracy(float accuracy) {
        this.accuracy = accuracy;
    }
    public float getRate() {
        return rate;
    }

    public void setRate(float rate) {
        this.rate = rate;
    }


}