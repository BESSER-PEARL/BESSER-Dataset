





import java.util.List;
import java.util.ArrayList;

public class FollowUpSubscriber  {

    private None location;
    private None user;
    private String followUpId;



    public FollowUpSubscriber(
        None location,        None user,        String followUpId    ) {
        this.location = location;
        this.user = user;
        this.followUpId = followUpId;
    }


    public None getLocation() {
        return location;
    }

    public void setLocation(None location) {
        this.location = location;
    }
    public None getUser() {
        return user;
    }

    public void setUser(None user) {
        this.user = user;
    }
    public String getFollowupid() {
        return followUpId;
    }

    public void setFollowupid(String followUpId) {
        this.followUpId = followUpId;
    }


}