




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shipTo;
    private LocalDate ordered;
    private float total;
    private None status;
    private int number;
    private boolean shipped;





    private Account account;




    private List<Payment> payments;


    public Order(
        String shipTo,        LocalDate ordered,        float total,        None status,        int number,        boolean shipped    ) {
        this.shipTo = shipTo;
        this.ordered = ordered;
        this.total = total;
        this.status = status;
        this.number = number;
        this.shipped = shipped;
        this.payments = new ArrayList<>();
    }

    public Order(
        String shipTo,        LocalDate ordered,        float total,        None status,        int number,        boolean shipped        ArrayList<Payment> payments    ) {
        this.shipTo = shipTo;
        this.ordered = ordered;
        this.total = total;
        this.status = status;
        this.number = number;
        this.shipped = shipped;
        this.payments = payments;
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