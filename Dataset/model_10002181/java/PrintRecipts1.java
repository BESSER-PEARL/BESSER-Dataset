





import java.util.List;
import java.util.ArrayList;

public class PrintRecipts1  {

    private String time;
    private int CustomerID;
    private int Quantity;
    private String Dishname;
    private String PaymentID;
    private String date;
    private String Amount;





    private Payment1 payment1;


    public PrintRecipts1(
        String time,        int CustomerID,        int Quantity,        String Dishname,        String PaymentID,        String date,        String Amount    ) {
        this.time = time;
        this.CustomerID = CustomerID;
        this.Quantity = Quantity;
        this.Dishname = Dishname;
        this.PaymentID = PaymentID;
        this.date = date;
        this.Amount = Amount;
    }


    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public int getCustomerid() {
        return CustomerID;
    }

    public void setCustomerid(int CustomerID) {
        this.CustomerID = CustomerID;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }
    public String getDishname() {
        return Dishname;
    }

    public void setDishname(String Dishname) {
        this.Dishname = Dishname;
    }
    public String getPaymentid() {
        return PaymentID;
    }

    public void setPaymentid(String PaymentID) {
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

    public Payment1 getPayment1() {
        return payment1;
    }

    public void setPayment1(Payment1 payment1) {
        this.payment1 = payment1;
    }

}