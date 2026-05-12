





import java.util.List;
import java.util.ArrayList;

public class Payment1  {

    private int CustomerID;
    private int PaymentID;
    private String date;
    private String Amount;
    private int OrderID;
    private String time;



    public Payment1(
        int CustomerID,        int PaymentID,        String date,        String Amount,        int OrderID,        String time    ) {
        this.CustomerID = CustomerID;
        this.PaymentID = PaymentID;
        this.date = date;
        this.Amount = Amount;
        this.OrderID = OrderID;
        this.time = time;
    }


    public int getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(int CustomerID) {
        this.CustomerID = CustomerID;
    }
    public int getPaymentid() {
        return PaymentID;
    }

    public void setPaymentid(int PaymentID) {
        this.PaymentID = PaymentID;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public int getOrderid() {
        return OrderID;
    }

    public void setOrderid(int OrderID) {
        this.OrderID = OrderID;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }


}