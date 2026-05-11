





import java.util.List;
import java.util.ArrayList;

public class pokerleague_InvitationEvent extends IdentifiableEntity {

    private boolean sent;
    private String eventType;
    private String eventTime;





    private pokerleague_Invitation pokerleague_invitation;




    private pokerleague_Invitation pokerleague_invitation;


    public pokerleague_InvitationEvent(
        boolean sent,        String eventType,        String eventTime    ) {
        super(
        );
        this.sent = sent;
        this.eventType = eventType;
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
    public String getEventtime() {
        return eventTime;
    }

    public void setEventtime(String eventTime) {
        this.eventTime = eventTime;
    }

    public pokerleague_Invitation getPokerleague_invitation() {
        return pokerleague_invitation;
    }

    public void setPokerleague_invitation(pokerleague_Invitation pokerleague_invitation) {
        this.pokerleague_invitation = pokerleague_invitation;
    }
    public pokerleague_Invitation getPokerleague_invitation() {
        return pokerleague_invitation;
    }

    public void setPokerleague_invitation(pokerleague_Invitation pokerleague_invitation) {
        this.pokerleague_invitation = pokerleague_invitation;
    }

}