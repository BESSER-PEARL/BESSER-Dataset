





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String FullName;
    private int PostCode;
    private String CreditCard;
    private String Address;
    private String Cellphone;





    private List<Order> orders;


    public Customer(
        String FullName,        int PostCode,        String CreditCard,        String Address,        String Cellphone    ) {
        this.FullName = FullName;
        this.PostCode = PostCode;
        this.CreditCard = CreditCard;
        this.Address = Address;
        this.Cellphone = Cellphone;
        this.orders = new ArrayList<>();
    }

    public Customer(
        String FullName,        int PostCode,        String CreditCard,        String Address,        String Cellphone        ArrayList<Order> orders    ) {
        this.FullName = FullName;
        this.PostCode = PostCode;
        this.CreditCard = CreditCard;
        this.Address = Address;
        this.Cellphone = Cellphone;
        this.orders = orders;
    }

    public String getFullname() {
        return FullName;
    }

    public void setFullname(String FullName) {
        this.FullName = FullName;
    }
    public int getPostcode() {
        return PostCode;
    }

    public void setPostcode(int PostCode) {
        this.PostCode = PostCode;
    }
    public String getCreditcard() {
        return CreditCard;
    }

    public void setCreditcard(String CreditCard) {
        this.CreditCard = CreditCard;
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

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}