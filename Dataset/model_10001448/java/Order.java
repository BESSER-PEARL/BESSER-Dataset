




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private LocalDate ordered;
    private None status;
    private int number;
    private float total;





    private Payment payment;




    private Account account;


    public Order(
        LocalDate ordered,        None status,        int number,        float total    ) {
        this.ordered = ordered;
        this.status = status;
        this.number = number;
        this.total = total;
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

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}