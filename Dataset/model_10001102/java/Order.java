




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private LocalDate ordered;
    private None status;
    private float total;
    private boolean shipped;
    private String shipTo;
    private int number;





    private Payment payment;




    private Account account;


    public Order(
        LocalDate ordered,        None status,        float total,        boolean shipped,        String shipTo,        int number    ) {
        this.ordered = ordered;
        this.status = status;
        this.total = total;
        this.shipped = shipped;
        this.shipTo = shipTo;
        this.number = number;
    }


    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
    }
    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
        this.shipTo = shipTo;
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