





import java.util.List;
import java.util.ArrayList;

public class kiosk  {

    private None discount;
    private None saving;
    private String newsletters;





    private Owner owner;




    private List<customer> customers;




    private compuer compuer;


    public kiosk(
        None discount,        None saving,        String newsletters    ) {
        this.discount = discount;
        this.saving = saving;
        this.newsletters = newsletters;
        this.customers = new ArrayList<>();
    }

    public kiosk(
        None discount,        None saving,        String newsletters        ArrayList<customer> customers    ) {
        this.discount = discount;
        this.saving = saving;
        this.newsletters = newsletters;
        this.customers = customers;
    }

    public None getDiscount() {
        return discount;
    }

    public void setDiscount(None discount) {
        this.discount = discount;
    }
    public None getSaving() {
        return saving;
    }

    public void setSaving(None saving) {
        this.saving = saving;
    }
    public String getNewsletters() {
        return newsletters;
    }

    public void setNewsletters(String newsletters) {
        this.newsletters = newsletters;
    }

    public Owner getOwner() {
        return owner;
    }

    public void setOwner(Owner owner) {
        this.owner = owner;
    }
    public List<customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }
    public compuer getCompuer() {
        return compuer;
    }

    public void setCompuer(compuer compuer) {
        this.compuer = compuer;
    }

}