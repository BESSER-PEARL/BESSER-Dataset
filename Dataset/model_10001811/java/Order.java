




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private LocalDate ordered;
    private boolean shipped;
    private String status;
    private String shipTo;
    private float total;
    private int number;





    private Account account;




    private ShoppingCart shoppingcart;




    private Payment payment;


    public Order(
        LocalDate ordered,        boolean shipped,        String status,        String shipTo,        float total,        int number    ) {
        this.ordered = ordered;
        this.shipped = shipped;
        this.status = status;
        this.shipTo = shipTo;
        this.total = total;
        this.number = number;
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
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
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
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}