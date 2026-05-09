





import java.util.List;
import java.util.ArrayList;

public class model_R4EMeetingData  {

    private String id;
    private String startTime;
    private int sentCount;
    private String body;
    private String receivers;
    private String subject;
    private String location;
    private int duration;
    private String sender;





    private model_R4EReview model_r4ereview;


    public model_R4EMeetingData(
        String id,        String startTime,        int sentCount,        String body,        String receivers,        String subject,        String location,        int duration,        String sender    ) {
        this.id = id;
        this.startTime = startTime;
        this.sentCount = sentCount;
        this.body = body;
        this.receivers = receivers;
        this.subject = subject;
        this.location = location;
        this.duration = duration;
        this.sender = sender;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public int getSentcount() {
        return sentCount;
    }

    public void setSentcount(int sentCount) {
        this.sentCount = sentCount;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getReceivers() {
        return receivers;
    }

    public void setReceivers(String receivers) {
        this.receivers = receivers;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public int getDuration() {
        return duration;
    }

    public void setDuration(int duration) {
        this.duration = duration;
    }
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }

    public model_R4EReview getModel_r4ereview() {
        return model_r4ereview;
    }

    public void setModel_r4ereview(model_R4EReview model_r4ereview) {
        this.model_r4ereview = model_r4ereview;
    }

}