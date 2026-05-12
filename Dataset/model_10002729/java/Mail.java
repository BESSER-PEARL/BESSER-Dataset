





import java.util.List;
import java.util.ArrayList;

public class Mail  {

    private String emailID;
    private String subject;
    private String sendTo;
    private String sendBy;





    private Admin admin;




    private Executive_Director executive_director;


    public Mail(
        String emailID,        String subject,        String sendTo,        String sendBy    ) {
        this.emailID = emailID;
        this.subject = subject;
        this.sendTo = sendTo;
        this.sendBy = sendBy;
    }


    public String getEmailid() {
        return emailID;
    }

    public void setEmailid(String emailID) {
        this.emailID = emailID;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }
    public String getSendto() {
        return sendTo;
    }

    public void setSendto(String sendTo) {
        this.sendTo = sendTo;
    }
    public String getSendby() {
        return sendBy;
    }

    public void setSendby(String sendBy) {
        this.sendBy = sendBy;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public Executive_Director getExecutive_director() {
        return executive_director;
    }

    public void setExecutive_director(Executive_Director executive_director) {
        this.executive_director = executive_director;
    }

}