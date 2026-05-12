





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String phonenumber;
    private String creditCardInfo;
    private String attribute;
    private String address;



    public Customer(
        String phonenumber,        String creditCardInfo,        String attribute,        String address    ) {
        this.phonenumber = phonenumber;
        this.creditCardInfo = creditCardInfo;
        this.attribute = attribute;
        this.address = address;
    }


    public String getPhonenumber() {
        return phonenumber;
    }

    public void setPhonenumber(String phonenumber) {
        this.phonenumber = phonenumber;
    }
    public String getCreditcardinfo() {
        return creditCardInfo;
    }

    public void setCreditcardinfo(String creditCardInfo) {
        this.creditCardInfo = creditCardInfo;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}