





import java.util.List;
import java.util.ArrayList;

public class pokerleague_InvitationEvent extends IdentifiableEntity {

    private String eventType;
    private String eventTime;
    private boolean sent;



    public pokerleague_InvitationEvent(
        String eventType,        String eventTime,        boolean sent    ) {
        super(
        );
        this.eventType = eventType;
        this.eventTime = eventTime;
        this.sent = sent;
    }


    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }
    public String getEventtime() {
        return eventTime;
    }

    public void setEventtime(String eventTime) {
        this.eventTime = eventTime;
    }
    public boolean getSent() {
        return sent;
    }

    public void setSent(boolean sent) {
        this.sent = sent;
    }


}