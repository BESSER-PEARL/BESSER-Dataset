





import java.util.List;
import java.util.ArrayList;

public class hairDressersRegSys_Discounts  {

    private int Percentage;
    private String Name;
    private String Description;





    private hairDressersRegSys_Customer hairdressersregsys_customer;




    private List<hairDressersRegSys_Invoice> hairdressersregsys_invoices;




    private hairDressersRegSys_Invoice hairdressersregsys_invoice;




    private List<hairDressersRegSys_Customer> hairdressersregsys_customers;


    public hairDressersRegSys_Discounts(
        int Percentage,        String Name,        String Description    ) {
        this.Percentage = Percentage;
        this.Name = Name;
        this.Description = Description;
        this.hairdressersregsys_invoices = new ArrayList<>();
        this.hairdressersregsys_customers = new ArrayList<>();
    }

    public hairDressersRegSys_Discounts(
        int Percentage,        String Name,        String Description        ArrayList<hairDressersRegSys_Invoice> hairdressersregsys_invoices,        ArrayList<hairDressersRegSys_Customer> hairdressersregsys_customers    ) {
        this.Percentage = Percentage;
        this.Name = Name;
        this.Description = Description;
        this.hairdressersregsys_invoices = hairdressersregsys_invoices;
        this.hairdressersregsys_customers = hairdressersregsys_customers;
    }

    public int getPercentage() {
        return Percentage;
    }

    public void setPercentage(int Percentage) {
        this.Percentage = Percentage;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }

    public hairDressersRegSys_Customer getHairdressersregsys_customer() {
        return hairdressersregsys_customer;
    }

    public void setHairdressersregsys_customer(hairDressersRegSys_Customer hairdressersregsys_customer) {
        this.hairdressersregsys_customer = hairdressersregsys_customer;
    }
    public List<hairDressersRegSys_Invoice> getHairdressersregsys_invoices() {
        return hairdressersregsys_invoices;
    }

    public void addHairdressersregsys_invoice(Hairdressersregsys_invoice hairdressersregsys_invoice) {
        this.hairdressersregsys_invoices.add(hairdressersregsys_invoice);
    }
    public hairDressersRegSys_Invoice getHairdressersregsys_invoice() {
        return hairdressersregsys_invoice;
    }

    public void setHairdressersregsys_invoice(hairDressersRegSys_Invoice hairdressersregsys_invoice) {
        this.hairdressersregsys_invoice = hairdressersregsys_invoice;
    }
    public List<hairDressersRegSys_Customer> getHairdressersregsys_customers() {
        return hairdressersregsys_customers;
    }

    public void addHairdressersregsys_customer(Hairdressersregsys_customer hairdressersregsys_customer) {
        this.hairdressersregsys_customers.add(hairdressersregsys_customer);
    }

}