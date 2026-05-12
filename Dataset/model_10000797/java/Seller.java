





import java.util.List;
import java.util.ArrayList;

public class Seller  {

    private String property_id;
    private String seller_id;



    public Seller(
        String property_id,        String seller_id    ) {
        this.property_id = property_id;
        this.seller_id = seller_id;
    }


    public String getProperty_id() {
        return property_id;
    }

    public void setProperty_id(String property_id) {
        this.property_id = property_id;
    }
    public String getSeller_id() {
        return seller_id;
    }

    public void setSeller_id(String seller_id) {
        this.seller_id = seller_id;
    }


}