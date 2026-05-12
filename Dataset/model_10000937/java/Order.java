




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private None status;
    private float total;
    private int number;
    private LocalDate ordered;
    private String shipTo;
    private boolean shipped;





    private Account account;




    private Payment payment;


    public Order(
        None status,        float total,        int number,        LocalDate ordered,        String shipTo,        boolean shipped    ) {
        this.status = status;
        this.total = total;
        this.number = number;
        this.ordered = ordered;
        this.shipTo = shipTo;
        this.shipped = shipped;
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