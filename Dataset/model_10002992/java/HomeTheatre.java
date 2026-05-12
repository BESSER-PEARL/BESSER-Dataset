





import java.util.List;
import java.util.ArrayList;

public class HomeTheatre  {

    private String HTID;





    private Speakers speakers;




    private List<System> systems;




    private TV tv;


    public HomeTheatre(
        String HTID    ) {
        this.HTID = HTID;
        this.systems = new ArrayList<>();
    }

    public HomeTheatre(
        String HTID        ArrayList<System> systems    ) {
        this.HTID = HTID;
        this.systems = systems;
    }

    public String getHtid() {
        return HTID;
    }

    public void setHtid(String HTID) {
        this.HTID = HTID;
    }

    public Speakers getSpeakers() {
        return speakers;
    }

    public void setSpeakers(Speakers speakers) {
        this.speakers = speakers;
    }
    public List<System> getSystems() {
        return systems;
    }

    public void addSystem(System system) {
        this.systems.add(system);
    }
    public TV getTv() {
        return tv;
    }

    public void setTv(TV tv) {
        this.tv = tv;
    }

}