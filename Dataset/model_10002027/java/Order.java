





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None customer;
    private None appliance;



    public Order(
        None customer,        None appliance    ) {
        this.customer = customer;
        this.appliance = appliance;
    }


    public None getCustomer() {
        return customer;
    }

    public void setCustomer(None customer) {
        this.customer = customer;
    }
    public None getAppliance() {
        return appliance;
    }

    public void setAppliance(None appliance) {
        this.appliance = appliance;
    }


}