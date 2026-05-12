





import java.util.List;
import java.util.ArrayList;

public class GSM_Module  {

    private float Update;
    private String CmdMatch;
    private String Status;





    private Microcontroller microcontroller;


    public GSM_Module(
        float Update,        String CmdMatch,        String Status    ) {
        this.Update = Update;
        this.CmdMatch = CmdMatch;
        this.Status = Status;
    }


    public float getUpdate() {
        return Update;
    }

    public void setUpdate(float Update) {
        this.Update = Update;
    }
    public String getCmdmatch() {
        return CmdMatch;
    }

    public void setCmdmatch(String CmdMatch) {
        this.CmdMatch = CmdMatch;
    }
    public String getStatus() {
        return Status;
    }

    public void setStatus(String Status) {
        this.Status = Status;
    }

    public Microcontroller getMicrocontroller() {
        return microcontroller;
    }

    public void setMicrocontroller(Microcontroller microcontroller) {
        this.microcontroller = microcontroller;
    }

}