





import java.util.List;
import java.util.ArrayList;

public class online_market  {

    private String product_type;
    private String product_price;
    private int register_id_card;
    private String customer_address;
    private String customer_name;





    private the_product the_product;


    public online_market(
        String product_type,        String product_price,        int register_id_card,        String customer_address,        String customer_name    ) {
        this.product_type = product_type;
        this.product_price = product_price;
        this.register_id_card = register_id_card;
        this.customer_address = customer_address;
        this.customer_name = customer_name;
    }


    public String getProduct_type() {
        return product_type;
    }

    public void setProduct_type(String product_type) {
        this.product_type = product_type;
    }
    public String getProduct_price() {
        return product_price;
    }

    public void setProduct_price(String product_price) {
        this.product_price = product_price;
    }
    public int getRegister_id_card() {
        return register_id_card;
    }

    public void setRegister_id_card(int register_id_card) {
        this.register_id_card = register_id_card;
    }
    public String getCustomer_address() {
        return customer_address;
    }

    public void setCustomer_address(String customer_address) {
        this.customer_address = customer_address;
    }
    public String getCustomer_name() {
        return customer_name;
    }

    public void setCustomer_name(String customer_name) {
        this.customer_name = customer_name;
    }

    public the_product getThe_product() {
        return the_product;
    }

    public void setThe_product(the_product the_product) {
        this.the_product = the_product;
    }

}