





import java.util.List;
import java.util.ArrayList;

public class HomeTheatre  {

    private String SSID;





    private Speakers speakers;




    private System system;


    public HomeTheatre(
        String SSID    ) {
        this.SSID = SSID;
    }


    public String getSsid() {
        return SSID;
    }

    public void setSsid(String SSID) {
        this.SSID = SSID;
    }

    public Speakers getSpeakers() {
        return speakers;
    }

    public void setSpeakers(Speakers speakers) {
        this.speakers = speakers;
    }
    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }

}