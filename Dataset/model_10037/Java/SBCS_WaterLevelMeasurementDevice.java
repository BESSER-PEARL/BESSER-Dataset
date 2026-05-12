





import java.util.List;
import java.util.ArrayList;

public class SBCS_WaterLevelMeasurementDevice  {

    private boolean ready;
    private float waterLevel;





    private SBCS_ControlProgram sbcs_controlprogram;




    private SBCS_SteamBoiler sbcs_steamboiler;




    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_ControlProgram sbcs_controlprogram;




    private SBCS_SteamBoiler sbcs_steamboiler;


    public SBCS_WaterLevelMeasurementDevice(
        boolean ready,        float waterLevel    ) {
        this.ready = ready;
        this.waterLevel = waterLevel;
    }


    public boolean getReady() {
        return ready;
    }

    public void setReady(boolean ready) {
        this.ready = ready;
    }
    public float getWaterlevel() {
        return waterLevel;
    }

    public void setWaterlevel(float waterLevel) {
        this.waterLevel = waterLevel;
    }

    public SBCS_ControlProgram getSbcs_controlprogram() {
        return sbcs_controlprogram;
    }

    public void setSbcs_controlprogram(SBCS_ControlProgram sbcs_controlprogram) {
        this.sbcs_controlprogram = sbcs_controlprogram;
    }
    public SBCS_SteamBoiler getSbcs_steamboiler() {
        return sbcs_steamboiler;
    }

    public void setSbcs_steamboiler(SBCS_SteamBoiler sbcs_steamboiler) {
        this.sbcs_steamboiler = sbcs_steamboiler;
    }
    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
    }
    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
    }
    public SBCS_ControlProgram getSbcs_controlprogram() {
        return sbcs_controlprogram;
    }

    public void setSbcs_controlprogram(SBCS_ControlProgram sbcs_controlprogram) {
        this.sbcs_controlprogram = sbcs_controlprogram;
    }
    public SBCS_SteamBoiler getSbcs_steamboiler() {
        return sbcs_steamboiler;
    }

    public void setSbcs_steamboiler(SBCS_SteamBoiler sbcs_steamboiler) {
        this.sbcs_steamboiler = sbcs_steamboiler;
    }

}