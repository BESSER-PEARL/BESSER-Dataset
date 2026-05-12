





import java.util.List;
import java.util.ArrayList;

public class Entertainment  {

    private int DeviceID;





    private List<Speakers> speakerss;




    private List<HomeTheatre> hometheatres;




    private List<TV> tvs;


    public Entertainment(
        int DeviceID    ) {
        this.DeviceID = DeviceID;
        this.speakerss = new ArrayList<>();
        this.hometheatres = new ArrayList<>();
        this.tvs = new ArrayList<>();
    }

    public Entertainment(
        int DeviceID        ArrayList<Speakers> speakerss,        ArrayList<HomeTheatre> hometheatres,        ArrayList<TV> tvs    ) {
        this.DeviceID = DeviceID;
        this.speakerss = speakerss;
        this.hometheatres = hometheatres;
        this.tvs = tvs;
    }

    public int getDeviceid() {
        return DeviceID;
    }

    public void setDeviceid(int DeviceID) {
        this.DeviceID = DeviceID;
    }

    public List<Speakers> getSpeakerss() {
        return speakerss;
    }

    public void addSpeakers(Speakers speakers) {
        this.speakerss.add(speakers);
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

}