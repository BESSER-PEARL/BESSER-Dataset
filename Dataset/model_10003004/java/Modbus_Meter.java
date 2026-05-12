





import java.util.List;
import java.util.ArrayList;

public class Modbus_Meter  {

    private int MAC_ID;



    public Modbus_Meter(
        int MAC_ID    ) {
        this.MAC_ID = MAC_ID;
    }


    public int getMac_id() {
        return MAC_ID;
    }

    public void setMac_id(int MAC_ID) {
        this.MAC_ID = MAC_ID;
    }


}