





import java.util.List;
import java.util.ArrayList;

public class RandL_LoyaltyProgram  {

    private String name;





    private RandL_Container_RandL randl_container_randl;




    private RandL_Customer randl_customer;




    private List<RandL_ServiceLevel> randl_servicelevels;




    private List<RandL_Customer> randl_customers;




    private RandL_ServiceLevel randl_servicelevel;


    public RandL_LoyaltyProgram(
        String name    ) {
        this.name = name;
        this.randl_servicelevels = new ArrayList<>();
        this.randl_customers = new ArrayList<>();
    }

    public RandL_LoyaltyProgram(
        String name        ArrayList<RandL_ServiceLevel> randl_servicelevels,        ArrayList<RandL_Customer> randl_customers    ) {
        this.name = name;
        this.randl_servicelevels = randl_servicelevels;
        this.randl_customers = randl_customers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public RandL_Container_RandL getRandl_container_randl() {
        return randl_container_randl;
    }

    public void setRandl_container_randl(RandL_Container_RandL randl_container_randl) {
        this.randl_container_randl = randl_container_randl;
    }
    public RandL_Customer getRandl_customer() {
        return randl_customer;
    }

    public void setRandl_customer(RandL_Customer randl_customer) {
        this.randl_customer = randl_customer;
    }
    public List<RandL_ServiceLevel> getRandl_servicelevels() {
        return randl_servicelevels;
    }

    public void addRandl_servicelevel(Randl_servicelevel randl_servicelevel) {
        this.randl_servicelevels.add(randl_servicelevel);
    }
    public List<RandL_Customer> getRandl_customers() {
        return randl_customers;
    }

    public void addRandl_customer(Randl_customer randl_customer) {
        this.randl_customers.add(randl_customer);
    }
    public RandL_ServiceLevel getRandl_servicelevel() {
        return randl_servicelevel;
    }

    public void setRandl_servicelevel(RandL_ServiceLevel randl_servicelevel) {
        this.randl_servicelevel = randl_servicelevel;
    }

}