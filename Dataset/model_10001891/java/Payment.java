





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int cardNo;
    private None cardType;
    private None customerName;
    private None customerName1;





    private customer customer;


    public Payment(
        int cardNo,        None cardType,        None customerName,        None customerName1    ) {
        this.cardNo = cardNo;
        this.cardType = cardType;
        this.customerName = customerName;
        this.customerName1 = customerName1;
    }


    public int getCardno() {
        return cardNo;
    }

    public void setCardno(int cardNo) {
        this.cardNo = cardNo;
    }
    public None getCardtype() {
        return cardType;
    }

    public void setCardtype(None cardType) {
        this.cardType = cardType;
    }
    public None getCustomername() {
        return customerName;
    }

    public void setCustomername(None customerName) {
        this.customerName = customerName;
    }
    public None getCustomername1() {
        return customerName1;
    }

    public void setCustomername1(None customerName1) {
        this.customerName1 = customerName1;
    }

    public customer getCustomer() {
        return customer;
    }

    public void setCustomer(customer customer) {
        this.customer = customer;
    }

}