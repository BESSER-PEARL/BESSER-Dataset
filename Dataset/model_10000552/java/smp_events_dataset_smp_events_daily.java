





import java.util.List;
import java.util.ArrayList;

public class smp_events_dataset_smp_events_daily  {

    private String profileid;
    private String eventsourcename;
    private String externalIds_id__used_as_apnid_;
    private String ExternalIds_Type;



    public smp_events_dataset_smp_events_daily(
        String profileid,        String eventsourcename,        String externalIds_id__used_as_apnid_,        String ExternalIds_Type    ) {
        this.profileid = profileid;
        this.eventsourcename = eventsourcename;
        this.externalIds_id__used_as_apnid_ = externalIds_id__used_as_apnid_;
        this.ExternalIds_Type = ExternalIds_Type;
    }


    public String getProfileid() {
        return profileid;
    }

    public void setProfileid(String profileid) {
        this.profileid = profileid;
    }
    public String getEventsourcename() {
        return eventsourcename;
    }

    public void setEventsourcename(String eventsourcename) {
        this.eventsourcename = eventsourcename;
    }
    public String getExternalids_id__used_as_apnid_() {
        return externalIds_id__used_as_apnid_;
    }

    public void setExternalids_id__used_as_apnid_(String externalIds_id__used_as_apnid_) {
        this.externalIds_id__used_as_apnid_ = externalIds_id__used_as_apnid_;
    }
    public String getExternalids_type() {
        return ExternalIds_Type;
    }

    public void setExternalids_type(String ExternalIds_Type) {
        this.ExternalIds_Type = ExternalIds_Type;
    }


}