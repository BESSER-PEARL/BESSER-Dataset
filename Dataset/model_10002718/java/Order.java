




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int number;
    private String shipTo;
    private boolean shipped;
    private LocalDate ordered;
    private None status;
    private float total;





    private Account account;




    private List<Payment> payments;


    public Order(
        int number,        String shipTo,        boolean shipped,        LocalDate ordered,        None status,        float total    ) {
        this.number = number;
        this.shipTo = shipTo;
        this.shipped = shipped;
        this.ordered = ordered;
        this.status = status;
        this.total = total;
        this.payments = new ArrayList<>();
    }

    public Order(
        int number,        String shipTo,        boolean shipped,        LocalDate ordered,        None status,        float total        ArrayList<Payment> payments    ) {
        this.number = number;
        this.shipTo = shipTo;
        this.shipped = shipped;
        this.ordered = ordered;
        this.status = status;
        this.total = total;
        this.payments = payments;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
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
    public LocalDate getOrdered() {
        return ordered;
    }

    public void setOrdered(LocalDate ordered) {
        this.ordered = ordered;
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