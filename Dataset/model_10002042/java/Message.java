





import java.util.List;
import java.util.ArrayList;

public class Message  {

    private int SenderID;
    private String MessageContent;
    private boolean Seen;
    private int ReceiverID;
    private boolean Deliverd;
    private int Time;





    private System_Controller system_controller;


    public Message(
        int SenderID,        String MessageContent,        boolean Seen,        int ReceiverID,        boolean Deliverd,        int Time    ) {
        this.SenderID = SenderID;
        this.MessageContent = MessageContent;
        this.Seen = Seen;
        this.ReceiverID = ReceiverID;
        this.Deliverd = Deliverd;
        this.Time = Time;
    }


    public int getSenderid() {
        return SenderID;
    }

    public void setSenderid(int SenderID) {
        this.SenderID = SenderID;
    }
    public String getMessagecontent() {
        return MessageContent;
    }

    public void setMessagecontent(String MessageContent) {
        this.MessageContent = MessageContent;
    }
    public boolean getSeen() {
        return Seen;
    }

    public void setSeen(boolean Seen) {
        this.Seen = Seen;
    }
    public int getReceiverid() {
        return ReceiverID;
    }

    public void setReceiverid(int ReceiverID) {
        this.ReceiverID = ReceiverID;
    }
    public boolean getDeliverd() {
        return Deliverd;
    }

    public void setDeliverd(boolean Deliverd) {
        this.Deliverd = Deliverd;
    }
    public int getTime() {
        return Time;
    }

    public void setTime(int Time) {
        this.Time = Time;
    }

    public System_Controller getSystem_controller() {
        return system_controller;
    }

    public void setSystem_controller(System_Controller system_controller) {
        this.system_controller = system_controller;
    }

}