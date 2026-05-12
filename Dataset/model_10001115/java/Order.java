




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private boolean shipped;
    private float total;
    private LocalDate ordered;
    private int number;
    private None status;
    private String shipTo;





    private Account account;




    private Payment payment;


    public Order(
        boolean shipped,        float total,        LocalDate ordered,        int number,        None status,        String shipTo    ) {
        this.shipped = shipped;
        this.total = total;
        this.ordered = ordered;
        this.number = number;
        this.status = status;
        this.shipTo = shipTo;
    }


    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
    }
    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
        this.shipTo = shipTo;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}