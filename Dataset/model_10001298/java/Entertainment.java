





import java.util.List;
import java.util.ArrayList;

public class Entertainment  {

    private int DeviceID;





    private List<TV> tvs;




    private List<Speakers> speakerss;




    private List<HomeTheatre> hometheatres;


    public Entertainment(
        int DeviceID    ) {
        this.DeviceID = DeviceID;
        this.tvs = new ArrayList<>();
        this.speakerss = new ArrayList<>();
        this.hometheatres = new ArrayList<>();
    }

    public Entertainment(
        int DeviceID        ArrayList<TV> tvs,        ArrayList<Speakers> speakerss,        ArrayList<HomeTheatre> hometheatres    ) {
        this.DeviceID = DeviceID;
        this.tvs = tvs;
        this.speakerss = speakerss;
        this.hometheatres = hometheatres;
    }

    public int getDeviceid() {
        return DeviceID;
    }

    public void setDeviceid(int DeviceID) {
        this.DeviceID = DeviceID;
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
    public List<HomeTheatre> getHometheatres() {
        return hometheatres;
    }

    public void addHometheatre(Hometheatre hometheatre) {
        this.hometheatres.add(hometheatre);
    }

}