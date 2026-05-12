




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shipTo;
    private float total;
    private boolean shipped;
    private int number;
    private None status;
    private LocalDate ordered;





    private Payment payment;




    private Account account;


    public Order(
        String shipTo,        float total,        boolean shipped,        int number,        None status,        LocalDate ordered    ) {
        this.shipTo = shipTo;
        this.total = total;
        this.shipped = shipped;
        this.number = number;
        this.status = status;
        this.ordered = ordered;
    }


    public String getShipto() {
        return shipTo;
    }

    public void setShipto(String shipTo) {
        this.shipTo = shipTo;
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
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
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