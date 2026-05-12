




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private LocalDate ordered;
    private String shipTo;
    private boolean shipped;
    private float total;
    private int number;
    private None status;





    private Account account;




    private Payment payment;


    public Order(
        LocalDate ordered,        String shipTo,        boolean shipped,        float total,        int number,        None status    ) {
        this.ordered = ordered;
        this.shipTo = shipTo;
        this.shipped = shipped;
        this.total = total;
        this.number = number;
        this.status = status;
    }


    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
    }
    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
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