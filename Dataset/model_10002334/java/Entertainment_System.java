





import java.util.List;
import java.util.ArrayList;

public class Entertainment_System  {

    private int DeviceID;





    private List<HomeTheatre> hometheatres;




    private List<TV> tvs;




    private List<Speakers> speakerss;


    public Entertainment_System(
        int DeviceID    ) {
        this.DeviceID = DeviceID;
        this.hometheatres = new ArrayList<>();
        this.tvs = new ArrayList<>();
        this.speakerss = new ArrayList<>();
    }

    public Entertainment_System(
        int DeviceID        ArrayList<HomeTheatre> hometheatres,        ArrayList<TV> tvs,        ArrayList<Speakers> speakerss    ) {
        this.DeviceID = DeviceID;
        this.hometheatres = hometheatres;
        this.tvs = tvs;
        this.speakerss = speakerss;
    }

    public int getDeviceid() {
        return DeviceID;
    }

    public void setDeviceid(int DeviceID) {
        this.DeviceID = DeviceID;
    }

    public List<HomeTheatre> getHometheatres() {
        return hometheatres;
    }

    public void addHometheatre(Hometheatre hometheatre) {
        this.hometheatres.add(hometheatre);
    }
    public List<TV> getTvs() {
        return tvs;
    }

    public void addTv(Tv tv) {
        this.tvs.add(tv);
    }
    public List<Speakers> getSpeakerss() {
        return speakerss;
    }

    public void addSpeakers(Speakers speakers) {
        this.speakerss.add(speakers);
    }

}