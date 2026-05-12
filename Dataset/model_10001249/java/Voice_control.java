





import java.util.List;
import java.util.ArrayList;

public class Voice_control  {

    private String MicID;





    private Smart_mirror smart_mirror;


    public Voice_control(
        String MicID    ) {
        this.MicID = MicID;
    }


    public String getMicid() {
        return MicID;
    }

    public void setMicid(String MicID) {
        this.MicID = MicID;
    }

    public Smart_mirror getSmart_mirror() {
        return smart_mirror;
    }

    public void setSmart_mirror(Smart_mirror smart_mirror) {
        this.smart_mirror = smart_mirror;
    }

}