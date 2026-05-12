





import java.util.List;
import java.util.ArrayList;

public class SBCS_WaterLevelMeaurementDevice_getLevel extends Transition {

    private float ret;





    private SBCS_WaterLevelMeasurementDevice sbcs_waterlevelmeasurementdevice;


    public SBCS_WaterLevelMeaurementDevice_getLevel(
        float ret    ) {
        super(
        );
        this.ret = ret;
    }


    public float getRet() {
        return ret;
    }

    public void setRet(float ret) {
        this.ret = ret;
    }

    public SBCS_WaterLevelMeasurementDevice getSbcs_waterlevelmeasurementdevice() {
        return sbcs_waterlevelmeasurementdevice;
    }

    public void setSbcs_waterlevelmeasurementdevice(SBCS_WaterLevelMeasurementDevice sbcs_waterlevelmeasurementdevice) {
        this.sbcs_waterlevelmeasurementdevice = sbcs_waterlevelmeasurementdevice;
    }

}