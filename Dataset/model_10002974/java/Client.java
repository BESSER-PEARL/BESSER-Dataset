





import java.util.List;
import java.util.ArrayList;

public class Client  {

    private String address;
    private String email;
    private String credit_card_info;
    private String shipping_info;
    private String customer;



    public Client(
        String address,        String email,        String credit_card_info,        String shipping_info,        String customer    ) {
        this.address = address;
        this.email = email;
        this.credit_card_info = credit_card_info;
        this.shipping_info = shipping_info;
        this.customer = customer;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public String getCredit_card_info() {
        return credit_card_info;
    }

    public void setCredit_card_info(String credit_card_info) {
        this.credit_card_info = credit_card_info;
    }
    public String getShipping_info() {
        return shipping_info;
    }

    public void setShipping_info(String shipping_info) {
        this.shipping_info = shipping_info;
    }
    public String getCustomer() {
        return customer;
    }

    public void setCustomer(String customer) {
        this.customer = customer;
    }


}