





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String email;
    private int phone;
    private String address;
    private String shippingInfo;
    private String name;
    private String creditCardInfo;





    private Portal portal;


    public Customer(
        String email,        int phone,        String address,        String shippingInfo,        String name,        String creditCardInfo    ) {
        this.email = email;
        this.phone = phone;
        this.address = address;
        this.shippingInfo = shippingInfo;
        this.name = name;
        this.creditCardInfo = creditCardInfo;
    }


    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getShippinginfo() {
        return shippingInfo;
    }

    public void setShippinginfo(String shippingInfo) {
        this.shippingInfo = shippingInfo;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCreditcardinfo() {
        return creditCardInfo;
    }

    public void setCreditcardinfo(String creditCardInfo) {
        this.creditCardInfo = creditCardInfo;
    }

    public Portal getPortal() {
        return portal;
    }

    public void setPortal(Portal portal) {
        this.portal = portal;
    }

}