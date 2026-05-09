





import java.util.List;
import java.util.ArrayList;

public class reviews_Change extends Dated {

    private String key;
    private String state;
    private String id;
    private String message;
    private String subject;



    public reviews_Change(
        String key,        String state,        String id,        String message,        String subject    ) {
        super(
        );
        this.key = key;
        this.state = state;
        this.id = id;
        this.message = message;
        this.subject = subject;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
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


}