





import java.util.List;
import java.util.ArrayList;

public class sale_by_instalment  {

    private int id_card;
    private String saled_product;
    private String customer_name;





    private the_product the_product;


    public sale_by_instalment(
        int id_card,        String saled_product,        String customer_name    ) {
        this.id_card = id_card;
        this.saled_product = saled_product;
        this.customer_name = customer_name;
    }


    public int getId_card() {
        return id_card;
    }

    public void setId_card(int id_card) {
        this.id_card = id_card;
    }
    public String getSaled_product() {
        return saled_product;
    }

    public void setSaled_product(String saled_product) {
        this.saled_product = saled_product;
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