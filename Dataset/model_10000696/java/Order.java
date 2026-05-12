




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int number;
    private boolean shipped;
    private LocalDate ordered;
    private float total;
    private String shipTo;
    private None status;





    private Payment payment;




    private Account account;


    public Order(
        int number,        boolean shipped,        LocalDate ordered,        float total,        String shipTo,        None status    ) {
        this.number = number;
        this.shipped = shipped;
        this.ordered = ordered;
        this.total = total;
        this.shipTo = shipTo;
        this.status = status;
    }


    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }
    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
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
    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
        this.shipTo = shipTo;
    }
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
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