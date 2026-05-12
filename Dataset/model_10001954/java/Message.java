





import java.util.List;
import java.util.ArrayList;

public class Message  {

    private String Max_Chars;
    private int ID_Message;
    private int ID_User;
    private String Mail;





    private User user;


    public Message(
        String Max_Chars,        int ID_Message,        int ID_User,        String Mail    ) {
        this.Max_Chars = Max_Chars;
        this.ID_Message = ID_Message;
        this.ID_User = ID_User;
        this.Mail = Mail;
    }


    public String getMax_chars() {
        return Max_Chars;
    }

    public void setMax_chars(String Max_Chars) {
        this.Max_Chars = Max_Chars;
    }
    public int getId_message() {
        return ID_Message;
    }

    public void setId_message(int ID_Message) {
        this.ID_Message = ID_Message;
    }
    public int getId_user() {
        return ID_User;
    }

    public void setId_user(int ID_User) {
        this.ID_User = ID_User;
    }
    public String getMail() {
        return Mail;
    }

    public void setMail(String Mail) {
        this.Mail = Mail;
    }

    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}