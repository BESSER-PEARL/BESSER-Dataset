





import java.util.List;
import java.util.ArrayList;

public class ordersystem_special_PreferredCustomer extends Customer {

    private String since;



    public ordersystem_special_PreferredCustomer(
        String since    ) {
        super(
        );
        this.since = since;
    }


    public String getSince() {
        return since;
    }

    public void setSince(String since) {
        this.since = since;
    }


}