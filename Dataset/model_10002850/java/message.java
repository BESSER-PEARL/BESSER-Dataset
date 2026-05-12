





import java.util.List;
import java.util.ArrayList;

public class message  {






    private Sent sent;




    private Inbox inbox;




    private Deleted deleted;


    public message(
    ) {
    }



    public Sent getSent() {
        return sent;
    }

    public void setSent(Sent sent) {
        this.sent = sent;
    }
    public Inbox getInbox() {
        return inbox;
    }

    public void setInbox(Inbox inbox) {
        this.inbox = inbox;
    }
    public Deleted getDeleted() {
        return deleted;
    }

    public void setDeleted(Deleted deleted) {
        this.deleted = deleted;
    }

}