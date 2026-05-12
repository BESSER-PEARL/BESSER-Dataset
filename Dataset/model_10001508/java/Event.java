





import java.util.List;
import java.util.ArrayList;

public class Event  {

    private String time;
    private String about;
    private String participants;
    private String placeName;
    private None id;
    private int participantCount;
    private String type;
    private String location;
    private String image;
    private None organizator;
    private String discussion;



    public Event(
        String time,        String about,        String participants,        String placeName,        None id,        int participantCount,        String type,        String location,        String image,        None organizator,        String discussion    ) {
        this.time = time;
        this.about = about;
        this.participants = participants;
        this.placeName = placeName;
        this.id = id;
        this.participantCount = participantCount;
        this.type = type;
        this.location = location;
        this.image = image;
        this.organizator = organizator;
        this.discussion = discussion;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getAbout() {
        return about;
    }

    public void setAbout(String about) {
        this.about = about;
    }
    public String getParticipants() {
        return participants;
    }

    public void setParticipants(String participants) {
        this.participants = participants;
    }
    public String getPlacename() {
        return placeName;
    }

    public void setPlacename(String placeName) {
        this.placeName = placeName;
    }
    public None getId() {
        return id;
    }

    public void setId(None id) {
        this.id = id;
    }
    public int getParticipantcount() {
        return participantCount;
    }

    public void setParticipantcount(int participantCount) {
        this.participantCount = participantCount;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public None getOrganizator() {
        return organizator;
    }

    public void setOrganizator(None organizator) {
        this.organizator = organizator;
    }
    public String getDiscussion() {
        return discussion;
    }

    public void setDiscussion(String discussion) {
        this.discussion = discussion;
    }


}