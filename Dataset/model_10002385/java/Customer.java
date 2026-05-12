





import java.util.List;
import java.util.ArrayList;

public class Customer  {

    private String customerAddress;
    private int customerPhone;
    private String customerName;
    private int customerId;
    private String customerPaymentInfo;





    private Shopping_Cart shopping_cart;




    private List<Search> searchs;




    private User user;


    public Customer(
        String customerAddress,        int customerPhone,        String customerName,        int customerId,        String customerPaymentInfo    ) {
        this.customerAddress = customerAddress;
        this.customerPhone = customerPhone;
        this.customerName = customerName;
        this.customerId = customerId;
        this.customerPaymentInfo = customerPaymentInfo;
        this.searchs = new ArrayList<>();
    }

    public Customer(
        String customerAddress,        int customerPhone,        String customerName,        int customerId,        String customerPaymentInfo        ArrayList<Search> searchs    ) {
        this.customerAddress = customerAddress;
        this.customerPhone = customerPhone;
        this.customerName = customerName;
        this.customerId = customerId;
        this.customerPaymentInfo = customerPaymentInfo;
        this.searchs = searchs;
    }

    public String getCustomeraddress() {
        return customerAddress;
    }

    public void setCustomeraddress(String customerAddress) {
        this.customerAddress = customerAddress;
    }
    public int getCustomerphone() {
        return customerPhone;
    }

    public void setCustomerphone(int customerPhone) {
        this.customerPhone = customerPhone;
    }
    public String getCustomername() {
        return customerName;
    }

    public void setCustomername(String customerName) {
        this.customerName = customerName;
    }
    public int getCustomerid() {
        return customerId;
    }

    public void setCustomerid(int customerId) {
        this.customerId = customerId;
    }
    public String getCustomerpaymentinfo() {
        return customerPaymentInfo;
    }

    public void setCustomerpaymentinfo(String customerPaymentInfo) {
        this.customerPaymentInfo = customerPaymentInfo;
    }

    public Shopping_Cart getShopping_cart() {
        return shopping_cart;
    }

    public void setShopping_cart(Shopping_Cart shopping_cart) {
        this.shopping_cart = shopping_cart;
    }
    public List<Search> getSearchs() {
        return searchs;
    }

    public void addSearch(Search search) {
        this.searchs.add(search);
    }
    public User getUser() {
        return user;
    }

    public void setUser(User user) {
        this.user = user;
    }

}