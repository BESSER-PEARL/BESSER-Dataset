




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int number;
    private String shipTo;
    private float total;
    private None status;
    private LocalDate ordered;
    private boolean shipped;





    private List<Payment> payments;




    private Account account;


    public Order(
        int number,        String shipTo,        float total,        None status,        LocalDate ordered,        boolean shipped    ) {
        this.number = number;
        this.shipTo = shipTo;
        this.total = total;
        this.status = status;
        this.ordered = ordered;
        this.shipped = shipped;
        this.payments = new ArrayList<>();
    }

    public Order(
        int number,        String shipTo,        float total,        None status,        LocalDate ordered,        boolean shipped        ArrayList<Payment> payments    ) {
        this.number = number;
        this.shipTo = shipTo;
        this.total = total;
        this.status = status;
        this.ordered = ordered;
        this.shipped = shipped;
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