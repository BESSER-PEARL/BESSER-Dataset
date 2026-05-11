





import java.util.List;
import java.util.ArrayList;

public class pokerleague_InvitationEvent extends IdentifiableEntity {

    private String eventTime;
    private boolean sent;
    private String eventType;



    public pokerleague_InvitationEvent(
        String eventTime,        boolean sent,        String eventType    ) {
        super(
        );
        this.eventTime = eventTime;
        this.sent = sent;
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
    public String getEventtype() {
        return eventType;
    }

    public void setEventtype(String eventType) {
        this.eventType = eventType;
    }


}