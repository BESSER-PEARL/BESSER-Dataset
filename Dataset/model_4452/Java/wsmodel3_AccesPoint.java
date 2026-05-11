





import java.util.List;
import java.util.ArrayList;

public class wsmodel3_AccesPoint  {

    private String ssid;
    private String pass_;



    public wsmodel3_AccesPoint(
        String ssid,        String pass_    ) {
        this.ssid = ssid;
        this.pass_ = pass_;
    }


    public String getSsid() {
        return ssid;
    }

    public void setSsid(String ssid) {
        this.ssid = ssid;
    }
    public String getPass_() {
        return pass_;
    }

    public void setPass_(String pass_) {
        this.pass_ = pass_;
    }


}