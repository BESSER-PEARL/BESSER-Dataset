




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int number;
    private float total;
    private String shipTo;
    private LocalDate ordered;
    private boolean shipped;
    private None status;





    private Account account;




    private List<Payment> payments;


    public Order(
        int number,        float total,        String shipTo,        LocalDate ordered,        boolean shipped,        None status    ) {
        this.number = number;
        this.total = total;
        this.shipTo = shipTo;
        this.ordered = ordered;
        this.shipped = shipped;
        this.status = status;
        this.payments = new ArrayList<>();
    }

    public Order(
        int number,        float total,        String shipTo,        LocalDate ordered,        boolean shipped,        None status        ArrayList<Payment> payments    ) {
        this.number = number;
        this.total = total;
        this.shipTo = shipTo;
        this.ordered = ordered;
        this.shipped = shipped;
        this.status = status;
        this.payments = payments;
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