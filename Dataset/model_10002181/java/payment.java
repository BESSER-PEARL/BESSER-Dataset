





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private int PaymentID;
    private String time;
    private int OrderID;
    private String Amount;
    private int CustomerID;
    private String date;



    public Payment(
        int PaymentID,        String time,        int OrderID,        String Amount,        int CustomerID,        String date    ) {
        this.PaymentID = PaymentID;
        this.time = time;
        this.OrderID = OrderID;
        this.Amount = Amount;
        this.CustomerID = CustomerID;
        this.date = date;
    }


    public int getPaymentid() {
        return PaymentID;
    }

    public void setPaymentid(int PaymentID) {
        this.PaymentID = PaymentID;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public int getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(int CustomerID) {
        this.CustomerID = CustomerID;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }


}