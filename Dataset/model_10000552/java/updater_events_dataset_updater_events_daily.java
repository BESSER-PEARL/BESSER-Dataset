





import java.util.List;
import java.util.ArrayList;

public class updater_events_dataset_updater_events_daily  {

    private String segments_id;
    private String advertisername;
    private String sojernId;



    public updater_events_dataset_updater_events_daily(
        String segments_id,        String advertisername,        String sojernId    ) {
        this.segments_id = segments_id;
        this.advertisername = advertisername;
        this.sojernId = sojernId;
    }


    public String getSegments_id() {
        return segments_id;
    }

    public void setSegments_id(String segments_id) {
        this.segments_id = segments_id;
    }
    public String getAdvertisername() {
        return advertisername;
    }

    public void setAdvertisername(String advertisername) {
        this.advertisername = advertisername;
    }
    public String getSojernid() {
        return sojernId;
    }

    public void setSojernid(String sojernId) {
        this.sojernId = sojernId;
    }


}