




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shipTo;
    private LocalDate ordered;
    private float total;
    private None status;
    private boolean shipped;
    private int number;





    private Payment payment;




    private Account account;


    public Order(
        String shipTo,        LocalDate ordered,        float total,        None status,        boolean shipped,        int number    ) {
        this.shipTo = shipTo;
        this.ordered = ordered;
        this.total = total;
        this.status = status;
        this.shipped = shipped;
        this.number = number;
    }


    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
        this.shipTo = shipTo;
    }
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
    }
    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
    }
    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}