





import java.util.List;
import java.util.ArrayList;

public class Entertainment  {

    private int DeviceID;





    private List<HomeTheatre> hometheatres;




    private List<Speakers> speakerss;




    private List<TV> tvs;


    public Entertainment(
        int DeviceID    ) {
        this.DeviceID = DeviceID;
        this.hometheatres = new ArrayList<>();
        this.speakerss = new ArrayList<>();
        this.tvs = new ArrayList<>();
    }

    public Entertainment(
        int DeviceID        ArrayList<HomeTheatre> hometheatres,        ArrayList<Speakers> speakerss,        ArrayList<TV> tvs    ) {
        this.DeviceID = DeviceID;
        this.hometheatres = hometheatres;
        this.speakerss = speakerss;
        this.tvs = tvs;
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
    public List<Speakers> getSpeakerss() {
        return speakerss;
    }

    public void addSpeakers(Speakers speakers) {
        this.speakerss.add(speakers);
    }
    public List<TV> getTvs() {
        return tvs;
    }

    public void addTv(Tv tv) {
        this.tvs.add(tv);
    }

}