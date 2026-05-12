




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private float total;
    private String shipTo;
    private int number;
    private None status;
    private boolean shipped;
    private LocalDate ordered;





    private Payment payment;




    private Account account;


    public Order(
        float total,        String shipTo,        int number,        None status,        boolean shipped,        LocalDate ordered    ) {
        this.total = total;
        this.shipTo = shipTo;
        this.number = number;
        this.status = status;
        this.shipped = shipped;
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