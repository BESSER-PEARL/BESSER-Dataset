





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Invitation extends IdentifiableEntity {

    private String uuid;
    private int ordinal;
    private String reply;





    private pokerleague_InvitationEvent pokerleague_invitationevent;




    private pokerleague_Player pokerleague_player;




    private List<pokerleague_InvitationEvent> pokerleague_invitationevents;


    public pokerleague_Invitation(
        String uuid,        int ordinal,        String reply    ) {
        super(
        );
        this.uuid = uuid;
        this.ordinal = ordinal;
        this.reply = reply;
        this.pokerleague_invitationevents = new ArrayList<>();
    }

    public pokerleague_Invitation(
        String uuid,        int ordinal,        String reply        ArrayList<pokerleague_InvitationEvent> pokerleague_invitationevents    ) {
        this.uuid = uuid;
        this.ordinal = ordinal;
        this.reply = reply;
        this.pokerleague_invitationevents = pokerleague_invitationevents;
    }

    public String getUuid() {
        return uuid;
    }

    public void setUuid(String uuid) {
        this.uuid = uuid;
    }
    public int getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(int ordinal) {
        this.ordinal = ordinal;
    }
    public String getReply() {
        return reply;
    }

    public void setReply(String reply) {
        this.reply = reply;
    }

    public pokerleague_InvitationEvent getPokerleague_invitationevent() {
        return pokerleague_invitationevent;
    }

    public void setPokerleague_invitationevent(pokerleague_InvitationEvent pokerleague_invitationevent) {
        this.pokerleague_invitationevent = pokerleague_invitationevent;
    }
    public pokerleague_Player getPokerleague_player() {
        return pokerleague_player;
    }

    public void setPokerleague_player(pokerleague_Player pokerleague_player) {
        this.pokerleague_player = pokerleague_player;
    }
    public List<pokerleague_InvitationEvent> getPokerleague_invitationevents() {
        return pokerleague_invitationevents;
    }

    public void addPokerleague_invitationevent(Pokerleague_invitationevent pokerleague_invitationevent) {
        this.pokerleague_invitationevents.add(pokerleague_invitationevent);
    }

}