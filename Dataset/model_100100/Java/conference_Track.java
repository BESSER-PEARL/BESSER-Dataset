





import java.util.List;
import java.util.ArrayList;

public class conference_Track  {

    private String name;





    private conference_Conference conference_conference;


    public conference_Track(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public conference_Conference getConference_conference() {
        return conference_conference;
    }

    public void setConference_conference(conference_Conference conference_conference) {
        this.conference_conference = conference_conference;
    }

}