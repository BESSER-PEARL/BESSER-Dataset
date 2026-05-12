





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String CreditCard;
    private int PostCode;
    private String Cellphone;
    private String FullName;
    private String Address;





    private List<Order> orders;


    public Customer(
        String CreditCard,        int PostCode,        String Cellphone,        String FullName,        String Address    ) {
        this.CreditCard = CreditCard;
        this.PostCode = PostCode;
        this.Cellphone = Cellphone;
        this.FullName = FullName;
        this.Address = Address;
        this.orders = new ArrayList<>();
    }

    public Customer(
        String CreditCard,        int PostCode,        String Cellphone,        String FullName,        String Address        ArrayList<Order> orders    ) {
        this.CreditCard = CreditCard;
        this.PostCode = PostCode;
        this.Cellphone = Cellphone;
        this.FullName = FullName;
        this.Address = Address;
        this.orders = orders;
    }

    public String getCreditcard() {
        return CreditCard;
    }

    public void setCreditcard(String CreditCard) {
        this.CreditCard = CreditCard;
    }
    public int getPostcode() {
        return PostCode;
    }

    public void setPostcode(int PostCode) {
        this.PostCode = PostCode;
    }
    public String getCellphone() {
        return Cellphone;
    }

    public void setCellphone(String Cellphone) {
        this.Cellphone = Cellphone;
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