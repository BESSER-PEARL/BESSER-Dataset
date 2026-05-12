





import java.util.List;
import java.util.ArrayList;

public class SBCS_ControlProgram  {

    private String mode;
    private boolean pumpFailure;
    private boolean pumpControlerFailure;
    private boolean smdFailure;





    private SBCS_ControlProgram_Start sbcs_controlprogram_start;




    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_Snapshot sbcs_snapshot;


    public SBCS_ControlProgram(
        String mode,        boolean pumpFailure,        boolean pumpControlerFailure,        boolean smdFailure    ) {
        this.mode = mode;
        this.pumpFailure = pumpFailure;
        this.pumpControlerFailure = pumpControlerFailure;
        this.smdFailure = smdFailure;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public boolean getPumpfailure() {
        return pumpFailure;
    }

    public void setPumpfailure(boolean pumpFailure) {
        this.pumpFailure = pumpFailure;
    }
    public boolean getPumpcontrolerfailure() {
        return pumpControlerFailure;
    }

    public void setPumpcontrolerfailure(boolean pumpControlerFailure) {
        this.pumpControlerFailure = pumpControlerFailure;
    }
    public boolean getSmdfailure() {
        return smdFailure;
    }

    public void setSmdfailure(boolean smdFailure) {
        this.smdFailure = smdFailure;
    }

    public SBCS_ControlProgram_Start getSbcs_controlprogram_start() {
        return sbcs_controlprogram_start;
    }

    public void setSbcs_controlprogram_start(SBCS_ControlProgram_Start sbcs_controlprogram_start) {
        this.sbcs_controlprogram_start = sbcs_controlprogram_start;
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

}