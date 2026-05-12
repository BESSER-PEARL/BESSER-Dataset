





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String ShippingInfo;
    private String CustomerName;
    private String Address;
    private String CreditCartInfo;
    private String Email;
    private int AccountBalance;



    public Customer(
        String ShippingInfo,        String CustomerName,        String Address,        String CreditCartInfo,        String Email,        int AccountBalance    ) {
        this.ShippingInfo = ShippingInfo;
        this.CustomerName = CustomerName;
        this.Address = Address;
        this.CreditCartInfo = CreditCartInfo;
        this.Email = Email;
        this.AccountBalance = AccountBalance;
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
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
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
    public int getAccountbalance() {
        return AccountBalance;
    }

    public void setAccountbalance(int AccountBalance) {
        this.AccountBalance = AccountBalance;
    }


}