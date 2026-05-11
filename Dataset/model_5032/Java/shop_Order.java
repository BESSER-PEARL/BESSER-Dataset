





import java.util.List;
import java.util.ArrayList;

public class shop_Order  {

    private String comments;
    private String number;





    private shop_Customer shop_customer;


    public shop_Order(
        String comments,        String number    ) {
        this.comments = comments;
        this.number = number;
    }


    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    public shop_Customer getShop_customer() {
        return shop_customer;
    }

    public void setShop_customer(shop_Customer shop_customer) {
        this.shop_customer = shop_customer;
    }

}