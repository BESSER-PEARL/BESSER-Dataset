





import java.util.List;
import java.util.ArrayList;

public class RandL_Container_RandL  {






    private List<RandL_Customer> randl_customers;


    public RandL_Container_RandL(
    ) {
        this.randl_customers = new ArrayList<>();
    }

    public RandL_Container_RandL(
        ArrayList<RandL_Customer> randl_customers    ) {
        this.randl_customers = randl_customers;
    }


    public List<RandL_Customer> getRandl_customers() {
        return randl_customers;
    }

    public void addRandl_customer(Randl_customer randl_customer) {
        this.randl_customers.add(randl_customer);
    }

}