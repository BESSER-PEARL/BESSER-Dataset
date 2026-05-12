





import java.util.List;
import java.util.ArrayList;

public class Customercare  {

    private int no;
    private String address;





    private List<Customer> customers;


    public Customercare(
        int no,        String address    ) {
        this.no = no;
        this.address = address;
        this.customers = new ArrayList<>();
    }

    public Customercare(
        int no,        String address        ArrayList<Customer> customers    ) {
        this.no = no;
        this.address = address;
        this.customers = customers;
    }

    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}