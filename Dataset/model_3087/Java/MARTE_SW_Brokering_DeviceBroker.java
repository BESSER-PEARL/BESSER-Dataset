





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Brokering_DeviceBroker extends SwResource {

    private String isBuffered;
    private String name;
    private String accessPolicy;



    public MARTE_SW_Brokering_DeviceBroker(
        String isBuffered,        String name,        String accessPolicy    ) {
        super(
        );
        this.isBuffered = isBuffered;
        this.name = name;
        this.accessPolicy = accessPolicy;
    }


    public String getIsbuffered() {
        return isBuffered;
    }

    public void setIsbuffered(String isBuffered) {
        this.isBuffered = isBuffered;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAccesspolicy() {
        return accessPolicy;
    }

    public void setAccesspolicy(String accessPolicy) {
        this.accessPolicy = accessPolicy;
    }


}