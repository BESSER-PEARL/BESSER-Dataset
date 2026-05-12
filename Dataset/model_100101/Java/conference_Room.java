





import java.util.List;
import java.util.ArrayList;

public class conference_Room  {

    private String name;
    private int capacity;





    private conference_Site conference_site;


    public conference_Room(
        String name,        int capacity    ) {
        this.name = name;
        this.capacity = capacity;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public conference_Site getConference_site() {
        return conference_site;
    }

    public void setConference_site(conference_Site conference_site) {
        this.conference_site = conference_site;
    }

}