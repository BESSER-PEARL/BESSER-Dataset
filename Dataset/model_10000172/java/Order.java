




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None status;
    private boolean shipped;
    private String shipTo;
    private int number;
    private float total;
    private LocalDate ordered;





    private Payment payment;




    private Account account;


    public Order(
        None status,        boolean shipped,        String shipTo,        int number,        float total,        LocalDate ordered    ) {
        this.status = status;
        this.shipped = shipped;
        this.shipTo = shipTo;
        this.number = number;
        this.total = total;
        this.ordered = ordered;
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