





import java.util.List;
import java.util.ArrayList;

public class moba_MobaGeofenceTrigger extends MobaTrigger {

    private String eventType;



    public moba_MobaGeofenceTrigger(
        String eventType    ) {
        super(
        );
        this.eventType = eventType;
    }


    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }


}