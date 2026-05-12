





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String Cellphone;
    private int PostCode;
    private String CreditCard;
    private String FullName;
    private String Address;





    private List<Order> orders;


    public Customer(
        String Cellphone,        int PostCode,        String CreditCard,        String FullName,        String Address    ) {
        this.Cellphone = Cellphone;
        this.PostCode = PostCode;
        this.CreditCard = CreditCard;
        this.FullName = FullName;
        this.Address = Address;
        this.orders = new ArrayList<>();
    }

    public Customer(
        String Cellphone,        int PostCode,        String CreditCard,        String FullName,        String Address        ArrayList<Order> orders    ) {
        this.Cellphone = Cellphone;
        this.PostCode = PostCode;
        this.CreditCard = CreditCard;
        this.FullName = FullName;
        this.Address = Address;
        this.orders = orders;
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
    public String getCreditcard() {
        return CreditCard;
    }

    public void setCreditcard(String CreditCard) {
        this.CreditCard = CreditCard;
    }
    public String getFullname() {
        return FullName;
    }

    public void setFullname(String FullName) {
        this.FullName = FullName;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public List<Order> getOrders() {
        return orders;
    }

    public void addOrder(Order order) {
        this.orders.add(order);
    }

}