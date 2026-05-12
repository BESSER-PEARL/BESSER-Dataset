





import java.util.List;
import java.util.ArrayList;

public class HomeTheatre  {

    private String HTID;





    private System system;




    private Speakers speakers;




    private TV tv;


    public HomeTheatre(
        String HTID    ) {
        this.HTID = HTID;
    }


    public String getHtid() {
        return HTID;
    }

    public void setHtid(String HTID) {
        this.HTID = HTID;
    }

    public System getSystem() {
        return system;
    }

    public void setSystem(System system) {
        this.system = system;
    }
    public Speakers getSpeakers() {
        return speakers;
    }

    public void setSpeakers(Speakers speakers) {
        this.speakers = speakers;
    }
    public TV getTv() {
        return tv;
    }

    public void setTv(TV tv) {
        this.tv = tv;
    }

}