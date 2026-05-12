





import java.util.List;
import java.util.ArrayList;

public class profile_UserProfile  {

    private String name;
    private String credits;
    private String id;
    private String attribute;
    private String uid;



    public profile_UserProfile(
        String name,        String credits,        String id,        String attribute,        String uid    ) {
        this.name = name;
        this.credits = credits;
        this.id = id;
        this.attribute = attribute;
        this.uid = uid;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCredits() {
        return credits;
    }

    public void setCredits(String credits) {
        this.credits = credits;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }


}