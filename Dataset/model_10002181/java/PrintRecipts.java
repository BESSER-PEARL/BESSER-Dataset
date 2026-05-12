





import java.util.List;
import java.util.ArrayList;

public class PrintRecipts  {

    private String Amount;
    private String date;
    private String time;
    private String Dishname;
    private String PaymentID;
    private int CustomerID;
    private int Quantity;



    public PrintRecipts(
        String Amount,        String date,        String time,        String Dishname,        String PaymentID,        int CustomerID,        int Quantity    ) {
        this.Amount = Amount;
        this.date = date;
        this.time = time;
        this.Dishname = Dishname;
        this.PaymentID = PaymentID;
        this.CustomerID = CustomerID;
        this.Quantity = Quantity;
    }


    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
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


}