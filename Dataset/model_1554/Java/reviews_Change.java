





import java.util.List;
import java.util.ArrayList;

public class reviews_Change extends Dated {

    private String state;
    private String key;
    private String message;
    private String id;
    private String subject;



    public reviews_Change(
        String state,        String key,        String message,        String id,        String subject    ) {
        super(
        );
        this.state = state;
        this.key = key;
        this.message = message;
        this.id = id;
        this.subject = subject;
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
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }


}