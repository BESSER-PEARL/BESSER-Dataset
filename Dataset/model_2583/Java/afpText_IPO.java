





import java.util.List;
import java.util.ArrayList;

public class afpText_IPO extends structuredField {

    private String OvlyOrent;
    private String OvlyName;
    private String YolOset;
    private String XolOset;



    public afpText_IPO(
        String OvlyOrent,        String OvlyName,        String YolOset,        String XolOset    ) {
        super(
        );
        this.OvlyOrent = OvlyOrent;
        this.OvlyName = OvlyName;
        this.YolOset = YolOset;
        this.XolOset = XolOset;
    }


    public String getOvlyorent() {
        return OvlyOrent;
    }

    public void setOvlyorent(String OvlyOrent) {
        this.OvlyOrent = OvlyOrent;
    }
    public String getOvlyname() {
        return OvlyName;
    }

    public void setOvlyname(String OvlyName) {
        this.OvlyName = OvlyName;
    }
    public String getYoloset() {
        return YolOset;
    }

    public void setYoloset(String YolOset) {
        this.YolOset = YolOset;
    }
    public String getXoloset() {
        return XolOset;
    }

    public void setXoloset(String XolOset) {
        this.XolOset = XolOset;
    }


}