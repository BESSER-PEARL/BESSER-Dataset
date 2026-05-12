




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private boolean shipped;
    private None status;
    private float total;
    private LocalDate ordered;
    private String shipTo;
    private int number;





    private List<Payment> payments;




    private Account account;


    public Order(
        boolean shipped,        None status,        float total,        LocalDate ordered,        String shipTo,        int number    ) {
        this.shipped = shipped;
        this.status = status;
        this.total = total;
        this.ordered = ordered;
        this.shipTo = shipTo;
        this.number = number;
        this.payments = new ArrayList<>();
    }

    public Order(
        boolean shipped,        None status,        float total,        LocalDate ordered,        String shipTo,        int number        ArrayList<Payment> payments    ) {
        this.shipped = shipped;
        this.status = status;
        this.total = total;
        this.ordered = ordered;
        this.shipTo = shipTo;
        this.number = number;
        this.payments = payments;
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

    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}