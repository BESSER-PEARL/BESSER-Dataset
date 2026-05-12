




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order_Compute_Price  {

    private boolean shipped;
    private float total;
    private String shipTo;
    private int number;
    private LocalDate ordered;
    private None status;





    private Account account;




    private List<Payment> payments;


    public Order_Compute_Price(
        boolean shipped,        float total,        String shipTo,        int number,        LocalDate ordered,        None status    ) {
        this.shipped = shipped;
        this.total = total;
        this.shipTo = shipTo;
        this.number = number;
        this.ordered = ordered;
        this.status = status;
        this.payments = new ArrayList<>();
    }

    public Order_Compute_Price(
        boolean shipped,        float total,        String shipTo,        int number,        LocalDate ordered,        None status        ArrayList<Payment> payments    ) {
        this.shipped = shipped;
        this.total = total;
        this.shipTo = shipTo;
        this.number = number;
        this.ordered = ordered;
        this.status = status;
        this.payments = payments;
    }

    public boolean getShipped() {
        return shipped;
    }

    public void setShipped(boolean shipped) {
        this.shipped = shipped;
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