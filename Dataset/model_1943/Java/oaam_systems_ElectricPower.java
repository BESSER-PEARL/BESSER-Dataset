





import java.util.List;
import java.util.ArrayList;

public class oaam_systems_ElectricPower extends InformationPower {

    private int nPhases;
    private float voltage;
    private float current;
    private float frequency;



    public oaam_systems_ElectricPower(
        int nPhases,        float voltage,        float current,        float frequency    ) {
        super(
        );
        this.nPhases = nPhases;
        this.voltage = voltage;
        this.current = current;
        this.frequency = frequency;
    }


    public int getNphases() {
        return nPhases;
    }

    public void setNphases(int nPhases) {
        this.nPhases = nPhases;
    }
    public float getVoltage() {
        return voltage;
    }

    public void setVoltage(float voltage) {
        this.voltage = voltage;
    }
    public float getCurrent() {
        return current;
    }

    public void setCurrent(float current) {
        this.current = current;
    }
    public float getFrequency() {
        return frequency;
    }

    public void setFrequency(float frequency) {
        this.frequency = frequency;
    }


}