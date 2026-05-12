





import java.util.List;
import java.util.ArrayList;

public class Customercare  {

    private String address;
    private int no;





    private List<Customer> customers;


    public Customercare(
        String address,        int no    ) {
        this.address = address;
        this.no = no;
        this.customers = new ArrayList<>();
    }

    public Customercare(
        String address,        int no        ArrayList<Customer> customers    ) {
        this.address = address;
        this.no = no;
        this.customers = customers;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getNo() {
        return no;
    }

    public void setNo(int no) {
        this.no = no;
    }

    public List<Customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}