





import java.util.List;
import java.util.ArrayList;

public class SBCS_Pump  {

    private String mode;
    private boolean ready;
    private float capacity;





    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_ControlProgram sbcs_controlprogram;




    private SBCS_Snapshot sbcs_snapshot;




    private SBCS_ControlProgram sbcs_controlprogram;


    public SBCS_Pump(
        String mode,        boolean ready,        float capacity    ) {
        this.mode = mode;
        this.ready = ready;
        this.capacity = capacity;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public boolean getReady() {
        return ready;
    }

    public void setReady(boolean ready) {
        this.ready = ready;
    }
    public float getCapacity() {
        return capacity;
    }

    public void setCapacity(float capacity) {
        this.capacity = capacity;
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

}