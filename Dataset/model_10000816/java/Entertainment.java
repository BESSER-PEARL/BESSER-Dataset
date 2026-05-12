





import java.util.List;
import java.util.ArrayList;

public class Entertainment  {

    private int DeviceID;





    private List<HomeControl> homecontrols;




    private List<SwitchControl> switchcontrols;


    public Entertainment(
        int DeviceID    ) {
        this.DeviceID = DeviceID;
        this.homecontrols = new ArrayList<>();
        this.switchcontrols = new ArrayList<>();
    }

    public Entertainment(
        int DeviceID        ArrayList<HomeControl> homecontrols,        ArrayList<SwitchControl> switchcontrols    ) {
        this.DeviceID = DeviceID;
        this.homecontrols = homecontrols;
        this.switchcontrols = switchcontrols;
    }

    public int getDeviceid() {
        return DeviceID;
    }

    public void setDeviceid(int DeviceID) {
        this.DeviceID = DeviceID;
    }

    public List<HomeControl> getHomecontrols() {
        return homecontrols;
    }

    public void addHomecontrol(Homecontrol homecontrol) {
        this.homecontrols.add(homecontrol);
    }
    public List<SwitchControl> getSwitchcontrols() {
        return switchcontrols;
    }

    public void addSwitchcontrol(Switchcontrol switchcontrol) {
        this.switchcontrols.add(switchcontrol);
    }

}