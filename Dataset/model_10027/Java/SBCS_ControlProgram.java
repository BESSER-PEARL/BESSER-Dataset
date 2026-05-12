





import java.util.List;
import java.util.ArrayList;

public class SBCS_ControlProgram  {

    private boolean wlmdFailure;
    private String mode;





    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_SteamBoiler sbcs_steamboiler;




    private SBCS_Snapshot sbcs_snapshot;


    public SBCS_ControlProgram(
        boolean wlmdFailure,        String mode    ) {
        this.wlmdFailure = wlmdFailure;
        this.mode = mode;
    }


    public boolean getWlmdfailure() {
        return wlmdFailure;
    }

    public void setWlmdfailure(boolean wlmdFailure) {
        this.wlmdFailure = wlmdFailure;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }

    public SBCS_Snapshot getSbcs_snapshot() {
        return sbcs_snapshot;
    }

    public void setSbcs_snapshot(SBCS_Snapshot sbcs_snapshot) {
        this.sbcs_snapshot = sbcs_snapshot;
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

}