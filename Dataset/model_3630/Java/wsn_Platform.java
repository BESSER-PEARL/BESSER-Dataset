





import java.util.List;
import java.util.ArrayList;

public class wsn_Platform  {

    private String platform;
    private String mote;



    public wsn_Platform(
        String platform,        String mote    ) {
        this.platform = platform;
        this.mote = mote;
    }


    public String getPlatform() {
        return platform;
    }

    public void setPlatform(String platform) {
        this.platform = platform;
    }
    public String getMote() {
        return mote;
    }

    public void setMote(String mote) {
        this.mote = mote;
    }


}