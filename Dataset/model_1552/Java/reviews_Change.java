





import java.util.List;
import java.util.ArrayList;

public class reviews_Change extends Dated {

    private String state;
    private String key;
    private String message;
    private String subject;
    private String id;



    public reviews_Change(
        String state,        String key,        String message,        String subject,        String id    ) {
        super(
        );
        this.state = state;
        this.key = key;
        this.message = message;
        this.subject = subject;
        this.id = id;
    }


    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}