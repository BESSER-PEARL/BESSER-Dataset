





import java.util.List;
import java.util.ArrayList;

public class wsn_Mode  {

    private float destination;
    private String mode_t;





    private wsn_Communication wsn_communication;


    public wsn_Mode(
        float destination,        String mode_t    ) {
        this.destination = destination;
        this.mode_t = mode_t;
    }


    public float getDestination() {
        return destination;
    }

    public void setDestination(float destination) {
        this.destination = destination;
    }
    public String getMode_t() {
        return mode_t;
    }

    public void setMode_t(String mode_t) {
        this.mode_t = mode_t;
    }

    public wsn_Communication getWsn_communication() {
        return wsn_communication;
    }

    public void setWsn_communication(wsn_Communication wsn_communication) {
        this.wsn_communication = wsn_communication;
    }

}