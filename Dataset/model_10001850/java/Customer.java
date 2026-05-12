





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String creditCardInfo;
    private String address;
    private None search__;
    private None registration__;
    private String shippingInfo;
    private None login__;
    private String customerName;
    private String email;



    public Customer(
        String creditCardInfo,        String address,        None search__,        None registration__,        String shippingInfo,        None login__,        String customerName,        String email    ) {
        this.creditCardInfo = creditCardInfo;
        this.address = address;
        this.search__ = search__;
        this.registration__ = registration__;
        this.shippingInfo = shippingInfo;
        this.login__ = login__;
        this.customerName = customerName;
        this.email = email;
    }


    public String getCreditcardinfo() {
        return creditCardInfo;
    }

    public void setCreditcardinfo(String creditCardInfo) {
        this.creditCardInfo = creditCardInfo;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public None getSearch__() {
        return search__;
    }

    public void setSearch__(None search__) {
        this.search__ = search__;
    }
    public None getRegistration__() {
        return registration__;
    }

    public void setRegistration__(None registration__) {
        this.registration__ = registration__;
    }
    public String getShippinginfo() {
        return shippingInfo;
    }

    public void setShippinginfo(String shippingInfo) {
        this.shippingInfo = shippingInfo;
    }
    public None getLogin__() {
        return login__;
    }

    public void setLogin__(None login__) {
        this.login__ = login__;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }


}