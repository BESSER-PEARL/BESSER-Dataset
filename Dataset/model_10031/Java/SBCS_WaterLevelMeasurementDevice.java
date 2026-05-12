





import java.util.List;
import java.util.ArrayList;

public class SBCS_WaterLevelMeasurementDevice  {

    private float waterLevel;





    private SBCS_WaterLevelMeaurementDevice_getLevel sbcs_waterlevelmeaurementdevice_getlevel;


    public SBCS_WaterLevelMeasurementDevice(
        float waterLevel    ) {
        this.waterLevel = waterLevel;
    }


    public float getWaterlevel() {
        return waterLevel;
    }

    public void setWaterlevel(float waterLevel) {
        this.waterLevel = waterLevel;
    }

    public SBCS_WaterLevelMeaurementDevice_getLevel getSbcs_waterlevelmeaurementdevice_getlevel() {
        return sbcs_waterlevelmeaurementdevice_getlevel;
    }

    public void setSbcs_waterlevelmeaurementdevice_getlevel(SBCS_WaterLevelMeaurementDevice_getLevel sbcs_waterlevelmeaurementdevice_getlevel) {
        this.sbcs_waterlevelmeaurementdevice_getlevel = sbcs_waterlevelmeaurementdevice_getlevel;
    }

}