





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Address;
    private String Cellphone;
    private int PostCode;
    private String FullName;
    private String CreditCard;





    private List<Order> orders;


    public Customer(
        String Address,        String Cellphone,        int PostCode,        String FullName,        String CreditCard    ) {
        this.Address = Address;
        this.Cellphone = Cellphone;
        this.PostCode = PostCode;
        this.FullName = FullName;
        this.CreditCard = CreditCard;
        this.orders = new ArrayList<>();
    }

    public Customer(
        String Address,        String Cellphone,        int PostCode,        String FullName,        String CreditCard        ArrayList<Order> orders    ) {
        this.Address = Address;
        this.Cellphone = Cellphone;
        this.PostCode = PostCode;
        this.FullName = FullName;
        this.CreditCard = CreditCard;
        this.orders = orders;
    }

    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }
    public String getCellphone() {
        return Cellphone;
    }

    public void setCellphone(String Cellphone) {
        this.Cellphone = Cellphone;
    }
    public int getPostcode() {
        return PostCode;
    }

    public void setPostcode(int PostCode) {
        this.PostCode = PostCode;
    }
    public String getFullname() {
        return FullName;
    }

    public void setFullname(String FullName) {
        this.FullName = FullName;
    }
    public String getCreditcard() {
        return CreditCard;
    }

    public void setCreditcard(String CreditCard) {
        this.CreditCard = CreditCard;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}