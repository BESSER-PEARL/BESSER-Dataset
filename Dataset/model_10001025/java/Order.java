




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private float total;
    private String shipTo;
    private boolean shipped;
    private int number;
    private None status;
    private LocalDate ordered;





    private Account account;




    private Payment payment;


    public Order(
        float total,        String shipTo,        boolean shipped,        int number,        None status,        LocalDate ordered    ) {
        this.total = total;
        this.shipTo = shipTo;
        this.shipped = shipped;
        this.number = number;
        this.status = status;
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