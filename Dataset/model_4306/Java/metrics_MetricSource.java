





import java.util.List;
import java.util.ArrayList;

public class metrics_MetricSource  {

    private String lastContact;
    private String name;
    private String metrickind;
    private String lastPurge;
    private String location;



    public metrics_MetricSource(
        String lastContact,        String name,        String metrickind,        String lastPurge,        String location    ) {
        this.lastContact = lastContact;
        this.name = name;
        this.metrickind = metrickind;
        this.lastPurge = lastPurge;
        this.location = location;
    }


    public String getLastcontact() {
        return lastContact;
    }

    public void setLastcontact(String lastContact) {
        this.lastContact = lastContact;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMetrickind() {
        return metrickind;
    }

    public void setMetrickind(String metrickind) {
        this.metrickind = metrickind;
    }
    public String getLastpurge() {
        return lastPurge;
    }

    public void setLastpurge(String lastPurge) {
        this.lastPurge = lastPurge;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }


}