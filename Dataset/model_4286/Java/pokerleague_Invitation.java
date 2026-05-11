





import java.util.List;
import java.util.ArrayList;

public class pokerleague_Invitation extends IdentifiableEntity {

    private int ordinal;
    private String uuid;
    private String reply;



    public pokerleague_Invitation(
        int ordinal,        String uuid,        String reply    ) {
        super(
        );
        this.ordinal = ordinal;
        this.uuid = uuid;
        this.reply = reply;
    }


    public int getOrdinal() {
        return ordinal;
    }

    public void setOrdinal(int ordinal) {
        this.ordinal = ordinal;
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


}