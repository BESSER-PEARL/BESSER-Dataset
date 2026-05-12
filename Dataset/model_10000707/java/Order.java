




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shipTo;
    private float total;
    private None status;
    private int number;
    private boolean shipped;
    private LocalDate ordered;





    private Account account;




    private Payment payment;


    public Order(
        String shipTo,        float total,        None status,        int number,        boolean shipped,        LocalDate ordered    ) {
        this.shipTo = shipTo;
        this.total = total;
        this.status = status;
        this.number = number;
        this.shipped = shipped;
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
    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
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