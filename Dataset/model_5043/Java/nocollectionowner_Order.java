





import java.util.List;
import java.util.ArrayList;

public class nocollectionowner_Order  {

    private String number;
    private String comments;





    private nocollectionowner_Customer nocollectionowner_customer;


    public nocollectionowner_Order(
        String number,        String comments    ) {
        this.number = number;
        this.comments = comments;
    }


    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }

    public nocollectionowner_Customer getNocollectionowner_customer() {
        return nocollectionowner_customer;
    }

    public void setNocollectionowner_customer(nocollectionowner_Customer nocollectionowner_customer) {
        this.nocollectionowner_customer = nocollectionowner_customer;
    }

}