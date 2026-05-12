





import java.util.List;
import java.util.ArrayList;

public class CustomerInfo  {

    private int Cid;
    private String password;
    private String shippingaddress;
    private String billingaddress;
    private String Cname;





    private OnlineShopping onlineshopping;


    public CustomerInfo(
        int Cid,        String password,        String shippingaddress,        String billingaddress,        String Cname    ) {
        this.Cid = Cid;
        this.password = password;
        this.shippingaddress = shippingaddress;
        this.billingaddress = billingaddress;
        this.Cname = Cname;
    }


    public int getCid() {
        return Cid;
    }

    public void setCid(int Cid) {
        this.Cid = Cid;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getShippingaddress() {
        return shippingaddress;
    }

    public void setShippingaddress(String shippingaddress) {
        this.shippingaddress = shippingaddress;
    }
    public String getBillingaddress() {
        return billingaddress;
    }

    public void setBillingaddress(String billingaddress) {
        this.billingaddress = billingaddress;
    }
    public String getCname() {
        return Cname;
    }

    public void setCname(String Cname) {
        this.Cname = Cname;
    }

    public OnlineShopping getOnlineshopping() {
        return onlineshopping;
    }

    public void setOnlineshopping(OnlineShopping onlineshopping) {
        this.onlineshopping = onlineshopping;
    }

}