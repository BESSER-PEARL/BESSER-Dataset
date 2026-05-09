





import java.util.List;
import java.util.ArrayList;

public class RootElement_SupportTicket  {

    private String fixed;
    private String roomName;
    private String problemDescription;





    private RootElement_SupportTicketHandler rootelement_supporttickethandler;


    public RootElement_SupportTicket(
        String fixed,        String roomName,        String problemDescription    ) {
        this.fixed = fixed;
        this.roomName = roomName;
        this.problemDescription = problemDescription;
    }


    public String getFixed() {
        return fixed;
    }

    public void setFixed(String fixed) {
        this.fixed = fixed;
    }
    public String getRoomname() {
        return roomName;
    }

    public void setRoomname(String roomName) {
        this.roomName = roomName;
    }
    public String getProblemdescription() {
        return problemDescription;
    }

    public void setProblemdescription(String problemDescription) {
        this.problemDescription = problemDescription;
    }

    public RootElement_SupportTicketHandler getRootelement_supporttickethandler() {
        return rootelement_supporttickethandler;
    }

    public void setRootelement_supporttickethandler(RootElement_SupportTicketHandler rootelement_supporttickethandler) {
        this.rootelement_supporttickethandler = rootelement_supporttickethandler;
    }

}