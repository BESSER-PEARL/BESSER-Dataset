





import java.util.List;
import java.util.ArrayList;

public class jbatch_Stop  {

    private String on;
    private String restart;
    private String exitStatus;



    public jbatch_Stop(
        String on,        String restart,        String exitStatus    ) {
        this.on = on;
        this.restart = restart;
        this.exitStatus = exitStatus;
    }


    public String getOn() {
        return on;
    }

    public void setOn(String on) {
        this.on = on;
    }
    public String getRestart() {
        return restart;
    }

    public void setRestart(String restart) {
        this.restart = restart;
    }
    public String getExitstatus() {
        return exitStatus;
    }

    public void setExitstatus(String exitStatus) {
        this.exitStatus = exitStatus;
    }


}