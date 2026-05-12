





import java.util.List;
import java.util.ArrayList;

public class MicroPhone  {

    private String MicID;





    private System system;


    public MicroPhone(
        String MicID    ) {
        this.MicID = MicID;
    }


    public String getMicid() {
        return MicID;
    }

    public void setMicid(String MicID) {
        this.MicID = MicID;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}