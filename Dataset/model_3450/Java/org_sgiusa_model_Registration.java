





import java.util.List;
import java.util.ArrayList;

public class org_sgiusa_model_Registration  {

    private String cancelled;
    private String aborted;
    private String date;
    private String id;





    private User user;


    public org_sgiusa_model_Registration(
        String cancelled,        String aborted,        String date,        String id    ) {
        this.cancelled = cancelled;
        this.aborted = aborted;
        this.date = date;
        this.id = id;
    }


    public String getCancelled() {
        return cancelled;
    }

    public void setCancelled(String cancelled) {
        this.cancelled = cancelled;
    }
    public String getAborted() {
        return aborted;
    }

    public void setAborted(String aborted) {
        this.aborted = aborted;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}