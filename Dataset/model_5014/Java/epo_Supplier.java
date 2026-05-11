





import java.util.List;
import java.util.ArrayList;

public class epo_Supplier  {

    private String name;





    private List<epo_Customer> epo_customers;


    public epo_Supplier(
        String name    ) {
        this.name = name;
        this.epo_customers = new ArrayList<>();
    }

    public epo_Supplier(
        String name        ArrayList<epo_Customer> epo_customers    ) {
        this.name = name;
        this.epo_customers = epo_customers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<epo_Customer> getEpo_customers() {
        return epo_customers;
    }

    public void addEpo_customer(Epo_customer epo_customer) {
        this.epo_customers.add(epo_customer);
    }

}