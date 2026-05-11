





import java.util.List;
import java.util.ArrayList;

public class ftp_ElectricalValue extends TypedPortValue {

    private boolean anyVoltage;
    private boolean anyCurrent;
    private float current;
    private float voltage;



    public ftp_ElectricalValue(
        boolean anyVoltage,        boolean anyCurrent,        float current,        float voltage    ) {
        super(
        );
        this.anyVoltage = anyVoltage;
        this.anyCurrent = anyCurrent;
        this.current = current;
        this.voltage = voltage;
    }


    public boolean getAnyvoltage() {
        return anyVoltage;
    }

    public void setAnyvoltage(boolean anyVoltage) {
        this.anyVoltage = anyVoltage;
    }
    public boolean getAnycurrent() {
        return anyCurrent;
    }

    public void setAnycurrent(boolean anyCurrent) {
        this.anyCurrent = anyCurrent;
    }
    public float getCurrent() {
        return current;
    }

    public void setCurrent(float current) {
        this.current = current;
    }
    public float getVoltage() {
        return voltage;
    }

    public void setVoltage(float voltage) {
        this.voltage = voltage;
    }


}