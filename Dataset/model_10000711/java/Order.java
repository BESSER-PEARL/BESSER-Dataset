




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int number;
    private LocalDate ordered;
    private boolean shipped;
    private float total;
    private String shipTo;
    private None status;





    private Payment payment;




    private Account account;


    public Order(
        int number,        LocalDate ordered,        boolean shipped,        float total,        String shipTo,        None status    ) {
        this.number = number;
        this.ordered = ordered;
        this.shipped = shipped;
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
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
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