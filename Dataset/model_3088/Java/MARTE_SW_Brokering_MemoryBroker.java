





import java.util.List;
import java.util.ArrayList;

public class MARTE_SW_Brokering_MemoryBroker extends SwResource {

    private String accessPolicy;



    public MARTE_SW_Brokering_MemoryBroker(
        String accessPolicy    ) {
        super(
        );
        this.accessPolicy = accessPolicy;
    }


    public String getAccesspolicy() {
        return accessPolicy;
    }

    public void setAccesspolicy(String accessPolicy) {
        this.accessPolicy = accessPolicy;
    }


}