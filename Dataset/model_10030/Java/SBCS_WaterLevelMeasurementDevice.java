





import java.util.List;
import java.util.ArrayList;

public class SBCS_WaterLevelMeasurementDevice  {

    private float waterLevel;





    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_WaterLevelMeaurementDevice_getLevel sbcs_waterlevelmeaurementdevice_getlevel;




    private SBCS_SteamBoiler sbcs_steamboiler;


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

    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
    }
    public SBCS_WaterLevelMeaurementDevice_getLevel getSbcs_waterlevelmeaurementdevice_getlevel() {
        return sbcs_waterlevelmeaurementdevice_getlevel;
    }

    public void setSbcs_waterlevelmeaurementdevice_getlevel(SBCS_WaterLevelMeaurementDevice_getLevel sbcs_waterlevelmeaurementdevice_getlevel) {
        this.sbcs_waterlevelmeaurementdevice_getlevel = sbcs_waterlevelmeaurementdevice_getlevel;
    }
    public SBCS_SteamBoiler getSbcs_steamboiler() {
        return sbcs_steamboiler;
    }

    public void setSbcs_steamboiler(SBCS_SteamBoiler sbcs_steamboiler) {
        this.sbcs_steamboiler = sbcs_steamboiler;
    }

}