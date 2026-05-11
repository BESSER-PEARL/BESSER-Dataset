





import java.util.List;
import java.util.ArrayList;

public class accounting_Employee extends NamedElement {

    private String emails;





    private accounting_Project accounting_project;




    private accounting_Invoice accounting_invoice;


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

    public accounting_Project getAccounting_project() {
        return accounting_project;
    }

    public void setAccounting_project(accounting_Project accounting_project) {
        this.accounting_project = accounting_project;
    }
    public accounting_Invoice getAccounting_invoice() {
        return accounting_invoice;
    }

    public void setAccounting_invoice(accounting_Invoice accounting_invoice) {
        this.accounting_invoice = accounting_invoice;
    }

}