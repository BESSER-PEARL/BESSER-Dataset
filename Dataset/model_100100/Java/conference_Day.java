





import java.util.List;
import java.util.ArrayList;

public class conference_Day  {

    private String name;





    private conference_Conference conference_conference;


    public conference_Day(
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