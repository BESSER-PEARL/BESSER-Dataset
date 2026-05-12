





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int qty;
    private int ID;
    private String amount;
    private boolean blgl;
    private String price;
    private String type;
    private String attribute;
    private String Name;





    private List<Customer> customers;




    private Payment payment;


    public Product(
        int qty,        int ID,        String amount,        boolean blgl,        String price,        String type,        String attribute,        String Name    ) {
        this.qty = qty;
        this.ID = ID;
        this.amount = amount;
        this.blgl = blgl;
        this.price = price;
        this.type = type;
        this.attribute = attribute;
        this.Name = Name;
        this.customers = new ArrayList<>();
    }

    public Product(
        int qty,        int ID,        String amount,        boolean blgl,        String price,        String type,        String attribute,        String Name        ArrayList<Customer> customers    ) {
        this.qty = qty;
        this.ID = ID;
        this.amount = amount;
        this.blgl = blgl;
        this.price = price;
        this.type = type;
        this.attribute = attribute;
        this.Name = Name;
        this.customers = customers;
    }

    public int getQty() {
        return qty;
    }

    public void setQty(int qty) {
        this.qty = qty;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getAmount() {
        return amount;
    }

    public void setAmount(String amount) {
        this.amount = amount;
    }
    public boolean getBlgl() {
        return blgl;
    }

    public void setBlgl(boolean blgl) {
        this.blgl = blgl;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
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