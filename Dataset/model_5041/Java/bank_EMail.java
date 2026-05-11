





import java.util.List;
import java.util.ArrayList;

public class bank_EMail extends ContactMethod {

    private String eMailAddress;



    public bank_EMail(
        String eMailAddress    ) {
        super(
        );
        this.eMailAddress = eMailAddress;
    }


    public String getEmailaddress() {
        return eMailAddress;
    }

    public void setEmailaddress(String eMailAddress) {
        this.eMailAddress = eMailAddress;
    }


}