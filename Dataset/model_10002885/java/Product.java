





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String attribute;
    private int ID;
    private String type;
    private String price;
    private String amount;
    private int qty;
    private String Name;
    private boolean blgl;





    private List<Customer> customers;




    private Payment payment;


    public Product(
        String attribute,        int ID,        String type,        String price,        String amount,        int qty,        String Name,        boolean blgl    ) {
        this.attribute = attribute;
        this.ID = ID;
        this.type = type;
        this.price = price;
        this.amount = amount;
        this.qty = qty;
        this.Name = Name;
        this.blgl = blgl;
        this.customers = new ArrayList<>();
    }

    public Product(
        String attribute,        int ID,        String type,        String price,        String amount,        int qty,        String Name,        boolean blgl        ArrayList<Customer> customers    ) {
        this.attribute = attribute;
        this.ID = ID;
        this.type = type;
        this.price = price;
        this.amount = amount;
        this.qty = qty;
        this.Name = Name;
        this.blgl = blgl;
        this.customers = customers;
    }

    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public int getQty() {
        return qty;
    }

    public void setQty(int qty) {
        this.qty = qty;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getBlgl() {
        return blgl;
    }

    public void setBlgl(boolean blgl) {
        this.blgl = blgl;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}