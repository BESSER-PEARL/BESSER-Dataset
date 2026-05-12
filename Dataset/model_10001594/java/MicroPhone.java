





import java.util.List;
import java.util.ArrayList;

public class MicroPhone  {

    private String MicID;





    private IOT iot;


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

    public IOT getIot() {
        return iot;
    }

    public void setIot(IOT iot) {
        this.iot = iot;
    }

}