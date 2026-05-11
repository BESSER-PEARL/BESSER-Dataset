





import java.util.List;
import java.util.ArrayList;

public class ftp_AnalogBattery extends PrimitiveComponent {

    private float voltage;



    public ftp_AnalogBattery(
        float voltage    ) {
        super(
        );
        this.voltage = voltage;
    }


    public float getVoltage() {
        return voltage;
    }

    public void setVoltage(float voltage) {
        this.voltage = voltage;
    }


}