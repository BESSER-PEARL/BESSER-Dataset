





import java.util.List;
import java.util.ArrayList;

public class Mail  {

    private String subject;
    private String sendBy;
    private String emailID;
    private String sendTo;





    private SuperAdmin superadmin;




    private Admin admin;


    public Mail(
        String subject,        String sendBy,        String emailID,        String sendTo    ) {
        this.subject = subject;
        this.sendBy = sendBy;
        this.emailID = emailID;
        this.sendTo = sendTo;
    }


    public String getSubject() {
        return subject;
    }

    public void setSubject(String subject) {
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

    public SuperAdmin getSuperadmin() {
        return superadmin;
    }

    public void setSuperadmin(SuperAdmin superadmin) {
        this.superadmin = superadmin;
    }
    public Admin getAdmin() {
        return admin;
    }

    public void setAdmin(Admin admin) {
        this.admin = admin;
    }

}