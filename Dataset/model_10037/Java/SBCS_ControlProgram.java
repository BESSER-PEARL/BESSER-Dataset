





import java.util.List;
import java.util.ArrayList;

public class SBCS_ControlProgram  {

    private boolean failureDetected;
    private boolean pumpFailure;
    private boolean ready;
    private boolean wlmdFailure;
    private boolean smdFailure;
    private String mode;
    private boolean pumpControlerFailure;





    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_Snapshot sbcs_snapshot;


    public SBCS_ControlProgram(
        boolean failureDetected,        boolean pumpFailure,        boolean ready,        boolean wlmdFailure,        boolean smdFailure,        String mode,        boolean pumpControlerFailure    ) {
        this.failureDetected = failureDetected;
        this.pumpFailure = pumpFailure;
        this.ready = ready;
        this.wlmdFailure = wlmdFailure;
        this.smdFailure = smdFailure;
        this.mode = mode;
        this.pumpControlerFailure = pumpControlerFailure;
    }


    public boolean getFailuredetected() {
        return failureDetected;
    }

    public void setFailuredetected(boolean failureDetected) {
        this.failureDetected = failureDetected;
    }
    public boolean getPumpfailure() {
        return pumpFailure;
    }

    public void setPumpfailure(boolean pumpFailure) {
        this.pumpFailure = pumpFailure;
    }
    public boolean getReady() {
        return ready;
    }

    public void setReady(boolean ready) {
        this.ready = ready;
    }
    public boolean getWlmdfailure() {
        return wlmdFailure;
    }

    public void setWlmdfailure(boolean wlmdFailure) {
        this.wlmdFailure = wlmdFailure;
    }
    public boolean getSmdfailure() {
        return smdFailure;
    }

    public void setSmdfailure(boolean smdFailure) {
        this.smdFailure = smdFailure;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public boolean getPumpcontrolerfailure() {
        return pumpControlerFailure;
    }

    public void setPumpcontrolerfailure(boolean pumpControlerFailure) {
        this.pumpControlerFailure = pumpControlerFailure;
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