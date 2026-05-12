





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Customer  {

    private None E_mail;
    private None Name;
    private None Shippinginfo;
    private None Address;
    private String Phone;





    private List<online_shopping_Orders> online_shopping_orderss;


    public online_shopping_Customer(
        None E_mail,        None Name,        None Shippinginfo,        None Address,        String Phone    ) {
        this.E_mail = E_mail;
        this.Name = Name;
        this.Shippinginfo = Shippinginfo;
        this.Address = Address;
        this.Phone = Phone;
        this.online_shopping_orderss = new ArrayList<>();
    }

    public online_shopping_Customer(
        None E_mail,        None Name,        None Shippinginfo,        None Address,        String Phone        ArrayList<online_shopping_Orders> online_shopping_orderss    ) {
        this.E_mail = E_mail;
        this.Name = Name;
        this.Shippinginfo = Shippinginfo;
        this.Address = Address;
        this.Phone = Phone;
        this.online_shopping_orderss = online_shopping_orderss;
    }

    public None getE_mail() {
        return E_mail;
    }

    public void setE_mail(None E_mail) {
        this.E_mail = E_mail;
    }
    public None getName() {
        return Name;
    }

    public void setName(None Name) {
        this.Name = Name;
    }
    public None getShippinginfo() {
        return Shippinginfo;
    }

    public void setShippinginfo(None Shippinginfo) {
        this.Shippinginfo = Shippinginfo;
    }
    public None getAddress() {
        return Address;
    }

    public void setAddress(None Address) {
        this.Address = Address;
    }
    public String getPhone() {
        return Phone;
    }

    public void setPhone(String Phone) {
        this.Phone = Phone;
    }

    public List<online_shopping_Orders> getOnline_shopping_orderss() {
        return online_shopping_orderss;
    }

    public void addOnline_shopping_orders(Online_shopping_orders online_shopping_orders) {
        this.online_shopping_orderss.add(online_shopping_orders);
    }

}