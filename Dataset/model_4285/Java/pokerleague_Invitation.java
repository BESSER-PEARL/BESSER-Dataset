





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Invitation extends IdentifiableEntity {

    private String uuid;
    private String reply;
    private int ordinal;





    private List<pokerleague_InvitationEvent> pokerleague_invitationevents;




    private pokerleague_Player pokerleague_player;




    private pokerleague_InvitationEvent pokerleague_invitationevent;


    public pokerleague_Invitation(
        String uuid,        String reply,        int ordinal    ) {
        super(
        );
        this.uuid = uuid;
        this.reply = reply;
        this.ordinal = ordinal;
        this.pokerleague_invitationevents = new ArrayList<>();
    }

    public pokerleague_Invitation(
        String uuid,        String reply,        int ordinal        ArrayList<pokerleague_InvitationEvent> pokerleague_invitationevents    ) {
        this.uuid = uuid;
        this.reply = reply;
        this.ordinal = ordinal;
        this.pokerleague_invitationevents = pokerleague_invitationevents;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public String getReply() {
        return reply;
    }

    public void setReply(String reply) {
        this.reply = reply;
    }
    public int getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(int ordinal) {
        this.ordinal = ordinal;
    }

    public List<pokerleague_InvitationEvent> getPokerleague_invitationevents() {
        return pokerleague_invitationevents;
    }

    public void addPokerleague_invitationevent(Pokerleague_invitationevent pokerleague_invitationevent) {
        this.pokerleague_invitationevents.add(pokerleague_invitationevent);
    }
    public pokerleague_Player getPokerleague_player() {
        return pokerleague_player;
    }

    public void setPokerleague_player(pokerleague_Player pokerleague_player) {
        this.pokerleague_player = pokerleague_player;
    }
    public pokerleague_InvitationEvent getPokerleague_invitationevent() {
        return pokerleague_invitationevent;
    }

    public void setPokerleague_invitationevent(pokerleague_InvitationEvent pokerleague_invitationevent) {
        this.pokerleague_invitationevent = pokerleague_invitationevent;
    }

}