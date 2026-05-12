





import java.util.List;
import java.util.ArrayList;

public class HomeControl  {

    private String HTID;





    private LPGControl lpgcontrol;




    private System system;




    private SwitchControl switchcontrol;


    public HomeControl(
        String HTID    ) {
        this.HTID = HTID;
    }


    public String getHtid() {
        return HTID;
    }

    public void setHtid(String HTID) {
        this.HTID = HTID;
    }

    public LPGControl getLpgcontrol() {
        return lpgcontrol;
    }

    public void setLpgcontrol(LPGControl lpgcontrol) {
        this.lpgcontrol = lpgcontrol;
    }
    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }
    public SwitchControl getSwitchcontrol() {
        return switchcontrol;
    }

    public void setSwitchcontrol(SwitchControl switchcontrol) {
        this.switchcontrol = switchcontrol;
    }

}