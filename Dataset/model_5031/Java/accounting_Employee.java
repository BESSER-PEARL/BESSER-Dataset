





import java.util.List;
import java.util.ArrayList;

public class accounting_Employee extends NamedElement {

    private String emails;



    public accounting_Employee(
        String emails    ) {
        super(
        );
        this.emails = emails;
    }


    public String getEmails() {
        return emails;
    }

    public void setEmails(String emails) {
        this.emails = emails;
    }


}