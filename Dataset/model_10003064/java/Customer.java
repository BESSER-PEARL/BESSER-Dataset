





import java.util.List;
import java.util.ArrayList;

public class customer  {

    private String address;
    private int email_id;
    private String name;
    private String product_id;



    public customer(
        String address,        int email_id,        String name,        String product_id    ) {
        this.address = address;
        this.email_id = email_id;
        this.name = name;
        this.product_id = product_id;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getEmail_id() {
        return email_id;
    }

    public void setEmail_id(int email_id) {
        this.email_id = email_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getProduct_id() {
        return product_id;
    }

    public void setProduct_id(String product_id) {
        this.product_id = product_id;
    }


}