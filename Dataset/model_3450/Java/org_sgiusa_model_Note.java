





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Note  {

    private String creationDate;
    private String text;
    private String id;
    private String lastUpdate;





    private User user;


    public org_sgiusa_model_Note(
        String creationDate,        String text,        String id,        String lastUpdate    ) {
        this.creationDate = creationDate;
        this.text = text;
        this.id = id;
        this.lastUpdate = lastUpdate;
    }


    public String getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(String creationDate) {
        this.creationDate = creationDate;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLastupdate() {
        return lastUpdate;
    }

    public void setLastupdate(String lastUpdate) {
        this.lastUpdate = lastUpdate;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}