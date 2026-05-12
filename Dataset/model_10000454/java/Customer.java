





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String CreditCartInfo;
    private String Email;
    private String Address;
    private String ShippingInfo;
    private String CustomerName;
    private int AccountBalance;



    public Customer(
        String CreditCartInfo,        String Email,        String Address,        String ShippingInfo,        String CustomerName,        int AccountBalance    ) {
        this.CreditCartInfo = CreditCartInfo;
        this.Email = Email;
        this.Address = Address;
        this.ShippingInfo = ShippingInfo;
        this.CustomerName = CustomerName;
        this.AccountBalance = AccountBalance;
    }


    public String getCreditcartinfo() {
        return CreditCartInfo;
    }

    public void setCreditcartinfo(String CreditCartInfo) {
        this.CreditCartInfo = CreditCartInfo;
    }
    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getShippinginfo() {
        return ShippingInfo;
    }

    public void setShippinginfo(String ShippingInfo) {
        this.ShippingInfo = ShippingInfo;
    }
    public String getCustomername() {
        return CustomerName;
    }

    public void setCustomername(String CustomerName) {
        this.CustomerName = CustomerName;
    }
    public int getAccountbalance() {
        return AccountBalance;
    }

    public void setAccountbalance(int AccountBalance) {
        this.AccountBalance = AccountBalance;
    }


}