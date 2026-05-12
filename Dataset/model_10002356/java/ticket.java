





import java.util.List;
import java.util.ArrayList;

public class ticket  {

    private int tiketno_;
    private String dest;
    private int custid;
    private String attribute;
    private String source;





    private List<customer> customers;


    public ticket(
        int tiketno_,        String dest,        int custid,        String attribute,        String source    ) {
        this.tiketno_ = tiketno_;
        this.dest = dest;
        this.custid = custid;
        this.attribute = attribute;
        this.source = source;
        this.customers = new ArrayList<>();
    }

    public ticket(
        int tiketno_,        String dest,        int custid,        String attribute,        String source        ArrayList<customer> customers    ) {
        this.tiketno_ = tiketno_;
        this.dest = dest;
        this.custid = custid;
        this.attribute = attribute;
        this.source = source;
        this.customers = customers;
    }

    public int getTiketno_() {
        return tiketno_;
    }

    public void setTiketno_(int tiketno_) {
        this.tiketno_ = tiketno_;
    }
    public String getDest() {
        return dest;
    }

    public void setDest(String dest) {
        this.dest = dest;
    }
    public int getCustid() {
        return custid;
    }

    public void setCustid(int custid) {
        this.custid = custid;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public List<customer> getCustomers() {
        return customers;
    }

    public void addCustomer(Customer customer) {
        this.customers.add(customer);
    }

}