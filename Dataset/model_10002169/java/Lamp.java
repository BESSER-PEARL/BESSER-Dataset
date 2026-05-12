





import java.util.List;
import java.util.ArrayList;

public class Lamp  {

    private int LampID;





    private Relay relay;


    public Lamp(
        int LampID    ) {
        this.LampID = LampID;
    }


    public int getLampid() {
        return LampID;
    }

    public void setLampid(int LampID) {
        this.LampID = LampID;
    }

    public Relay getRelay() {
        return relay;
    }

    public void setRelay(Relay relay) {
        this.relay = relay;
    }

}