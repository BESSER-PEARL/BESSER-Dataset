





import java.util.List;
import java.util.ArrayList;

public class org_aries_common_EmailAddressList  {

    private String name;
    private String emailAddress;



    public org_aries_common_EmailAddressList(
        String name,        String emailAddress    ) {
        this.name = name;
        this.emailAddress = emailAddress;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmailaddress() {
        return emailAddress;
    }

    public void setEmailaddress(String emailAddress) {
        this.emailAddress = emailAddress;
    }


}