





import java.util.List;
import java.util.ArrayList;

public class wsn_Timer  {

    private int time;
    private String type;





    private wsn_Timing wsn_timing;


    public wsn_Timer(
        int time,        String type    ) {
        this.time = time;
        this.type = type;
    }


    public int getTime() {
        return time;
    }

    public void setTime(int time) {
        this.time = time;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public wsn_Timing getWsn_timing() {
        return wsn_timing;
    }

    public void setWsn_timing(wsn_Timing wsn_timing) {
        this.wsn_timing = wsn_timing;
    }

}