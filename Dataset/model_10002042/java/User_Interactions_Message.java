





import java.util.List;
import java.util.ArrayList;

public class User_Interactions_Message  {

    private boolean Deliverd;
    private String MessageContent;
    private boolean Seen;
    private int SenderID;
    private int ReceiverID;
    private int Time;





    private Users_User users_user;


    public User_Interactions_Message(
        boolean Deliverd,        String MessageContent,        boolean Seen,        int SenderID,        int ReceiverID,        int Time    ) {
        this.Deliverd = Deliverd;
        this.MessageContent = MessageContent;
        this.Seen = Seen;
        this.SenderID = SenderID;
        this.ReceiverID = ReceiverID;
        this.Time = Time;
    }


    public boolean getDeliverd() {
        return Deliverd;
    }

    public void setDeliverd(boolean Deliverd) {
        this.Deliverd = Deliverd;
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
    public int getSenderid() {
        return SenderID;
    }

    public void setSenderid(int SenderID) {
        this.SenderID = SenderID;
    }
    public int getReceiverid() {
        return ReceiverID;
    }

    public void setReceiverid(int ReceiverID) {
        this.ReceiverID = ReceiverID;
    }
    public int getTime() {
        return Time;
    }

    public void setTime(int Time) {
        this.Time = Time;
    }

    public Users_User getUsers_user() {
        return users_user;
    }

    public void setUsers_user(Users_User users_user) {
        this.users_user = users_user;
    }

}