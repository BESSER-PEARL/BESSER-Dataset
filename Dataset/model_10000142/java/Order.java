




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private LocalDate ordered;
    private float total;
    private String shipTo;
    private boolean shipped;
    private None status;
    private int number;





    private Account account;




    private List<Payment> payments;


    public Order(
        LocalDate ordered,        float total,        String shipTo,        boolean shipped,        None status,        int number    ) {
        this.ordered = ordered;
        this.total = total;
        this.shipTo = shipTo;
        this.shipped = shipped;
        this.status = status;
        this.number = number;
        this.payments = new ArrayList<>();
    }

    public Order(
        LocalDate ordered,        float total,        String shipTo,        boolean shipped,        None status,        int number        ArrayList<Payment> payments    ) {
        this.ordered = ordered;
        this.total = total;
        this.shipTo = shipTo;
        this.shipped = shipped;
        this.status = status;
        this.number = number;
        this.payments = payments;
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
    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
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

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }

}