





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_DocumentRoot  {

    private String mixed;





    private List<EmailAccount> emailaccounts;




    private List<Attachment> attachments;




    private List<ZipCode> zipcodes;


    public org_aries_common_DocumentRoot(
        String mixed    ) {
        this.mixed = mixed;
        this.emailaccounts = new ArrayList<>();
        this.attachments = new ArrayList<>();
        this.zipcodes = new ArrayList<>();
    }

    public org_aries_common_DocumentRoot(
        String mixed        ArrayList<EmailAccount> emailaccounts,        ArrayList<Attachment> attachments,        ArrayList<ZipCode> zipcodes    ) {
        this.mixed = mixed;
        this.emailaccounts = emailaccounts;
        this.attachments = attachments;
        this.zipcodes = zipcodes;
    }

    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public List<EmailAccount> getEmailaccounts() {
        return emailaccounts;
    }

    public void addEmailaccount(Emailaccount emailaccount) {
        this.emailaccounts.add(emailaccount);
    }
    public List<Attachment> getAttachments() {
        return attachments;
    }

    public void addAttachment(Attachment attachment) {
        this.attachments.add(attachment);
    }
    public List<ZipCode> getZipcodes() {
        return zipcodes;
    }

    public void addZipcode(Zipcode zipcode) {
        this.zipcodes.add(zipcode);
    }

}