





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Brokering_DeviceBroker extends SwResource {

    private String accessPolicy;
    private String isBuffered;



    public MARTE_SW_Brokering_DeviceBroker(
        String accessPolicy,        String isBuffered    ) {
        super(
        );
        this.accessPolicy = accessPolicy;
        this.isBuffered = isBuffered;
    }


    public String getAccesspolicy() {
        return accessPolicy;
    }

    public void setAccesspolicy(String accessPolicy) {
        this.accessPolicy = accessPolicy;
    }
    public String getIsbuffered() {
        return isBuffered;
    }

    public void setIsbuffered(String isBuffered) {
        this.isBuffered = isBuffered;
    }


}