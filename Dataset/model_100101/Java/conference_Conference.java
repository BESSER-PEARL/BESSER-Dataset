





import java.util.List;
import java.util.ArrayList;

public class conference_Conference  {

    private String name;
    private String overview;
    private String place;





    private List<conference_Site> conference_sites;




    private List<conference_Talk> conference_talks;




    private List<conference_Topic> conference_topics;


    public conference_Conference(
        String name,        String overview,        String place    ) {
        this.name = name;
        this.overview = overview;
        this.place = place;
        this.conference_sites = new ArrayList<>();
        this.conference_talks = new ArrayList<>();
        this.conference_topics = new ArrayList<>();
    }

    public conference_Conference(
        String name,        String overview,        String place        ArrayList<conference_Site> conference_sites,        ArrayList<conference_Talk> conference_talks,        ArrayList<conference_Topic> conference_topics    ) {
        this.name = name;
        this.overview = overview;
        this.place = place;
        this.conference_sites = conference_sites;
        this.conference_talks = conference_talks;
        this.conference_topics = conference_topics;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOverview() {
        return overview;
    }

    public void setOverview(String overview) {
        this.overview = overview;
    }
    public String getPlace() {
        return place;
    }

    public void setPlace(String place) {
        this.place = place;
    }

    public List<conference_Site> getConference_sites() {
        return conference_sites;
    }

    public void addConference_site(Conference_site conference_site) {
        this.conference_sites.add(conference_site);
    }
    public List<conference_Talk> getConference_talks() {
        return conference_talks;
    }

    public void addConference_talk(Conference_talk conference_talk) {
        this.conference_talks.add(conference_talk);
    }
    public List<conference_Topic> getConference_topics() {
        return conference_topics;
    }

    public void addConference_topic(Conference_topic conference_topic) {
        this.conference_topics.add(conference_topic);
    }

}