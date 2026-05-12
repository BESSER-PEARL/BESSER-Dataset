





import java.util.List;
import java.util.ArrayList;

public class WIFI_Sense  {

    private int WIFIID;





    private Door door;


    public WIFI_Sense(
        int WIFIID    ) {
        this.WIFIID = WIFIID;
    }


    public int getWifiid() {
        return WIFIID;
    }

    public void setWifiid(int WIFIID) {
        this.WIFIID = WIFIID;
    }

    public Door getDoor() {
        return door;
    }

    public void setDoor(Door door) {
        this.door = door;
    }

}