




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int number;
    private None status;
    private float total;
    private boolean shipped;
    private String shipTo;
    private LocalDate ordered;





    private Account account;




    private Payment payment;


    public Order(
        int number,        None status,        float total,        boolean shipped,        String shipTo,        LocalDate ordered    ) {
        this.number = number;
        this.status = status;
        this.total = total;
        this.shipped = shipped;
        this.shipTo = shipTo;
        this.ordered = ordered;
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