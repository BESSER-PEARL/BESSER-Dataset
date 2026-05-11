





import java.util.List;
import java.util.ArrayList;

public class customerDsl_Order  {

    private String channel;
    private String name;





    private customerDsl_CustomerDb customerdsl_customerdb;




    private customerDsl_Customer customerdsl_customer;


    public customerDsl_Order(
        String channel,        String name    ) {
        this.channel = channel;
        this.name = name;
    }


    public String getChannel() {
        return channel;
    }

    public void setChannel(String channel) {
        this.channel = channel;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public customerDsl_CustomerDb getCustomerdsl_customerdb() {
        return customerdsl_customerdb;
    }

    public void setCustomerdsl_customerdb(customerDsl_CustomerDb customerdsl_customerdb) {
        this.customerdsl_customerdb = customerdsl_customerdb;
    }
    public customerDsl_Customer getCustomerdsl_customer() {
        return customerdsl_customer;
    }

    public void setCustomerdsl_customer(customerDsl_Customer customerdsl_customer) {
        this.customerdsl_customer = customerdsl_customer;
    }

}