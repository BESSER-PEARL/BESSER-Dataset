





import java.util.List;
import java.util.ArrayList;

public class Mail  {

    private String sendBy;
    private String emailID;
    private String sendTo;
    private String subject;





    private Admin admin;




    private SuperAdmin superadmin;


    public Mail(
        String sendBy,        String emailID,        String sendTo,        String subject    ) {
        this.sendBy = sendBy;
        this.emailID = emailID;
        this.sendTo = sendTo;
        this.subject = subject;
    }


    public String getSendby() {
        return sendBy;
    }

    public void setSendby(String sendBy) {
        this.sendBy = sendBy;
    }
    public String getEmailid() {
        return emailID;
    }

    public void setEmailid(String emailID) {
        this.emailID = emailID;
    }
    public String getSendto() {
        return sendTo;
    }

    public void setSendto(String sendTo) {
        this.sendTo = sendTo;
    }
    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
        this.subject = subject;
    }

    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }
    public SuperAdmin getSuperadmin() {
        return superadmin;
    }

    public void setSuperadmin(SuperAdmin superadmin) {
        this.superadmin = superadmin;
    }

}