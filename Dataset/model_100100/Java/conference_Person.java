





import java.util.List;
import java.util.ArrayList;

public class conference_Person  {

    private String name;
    private String organisation;





    private conference_Conference conference_conference;




    private List<conference_Track> conference_tracks;




    private conference_Track conference_track;


    public conference_Person(
        String name,        String organisation    ) {
        this.name = name;
        this.organisation = organisation;
        this.conference_tracks = new ArrayList<>();
    }

    public conference_Person(
        String name,        String organisation        ArrayList<conference_Track> conference_tracks    ) {
        this.name = name;
        this.organisation = organisation;
        this.conference_tracks = conference_tracks;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOrganisation() {
        return organisation;
    }

    public void setOrganisation(String organisation) {
        this.organisation = organisation;
    }

    public conference_Conference getConference_conference() {
        return conference_conference;
    }

    public void setConference_conference(conference_Conference conference_conference) {
        this.conference_conference = conference_conference;
    }
    public List<conference_Track> getConference_tracks() {
        return conference_tracks;
    }

    public void addConference_track(Conference_track conference_track) {
        this.conference_tracks.add(conference_track);
    }
    public conference_Track getConference_track() {
        return conference_track;
    }

    public void setConference_track(conference_Track conference_track) {
        this.conference_track = conference_track;
    }

}