




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private boolean shipped;
    private int number;
    private float total;
    private String shipTo;
    private LocalDate ordered;
    private None status;





    private Payment payment;




    private Account account;


    public Order(
        boolean shipped,        int number,        float total,        String shipTo,        LocalDate ordered,        None status    ) {
        this.shipped = shipped;
        this.number = number;
        this.total = total;
        this.shipTo = shipTo;
        this.ordered = ordered;
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