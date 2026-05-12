




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shipTo;
    private int number;
    private float total;
    private String status;
    private boolean shipped;
    private LocalDate ordered;





    private Payment payment;




    private ShoppingCart shoppingcart;




    private Account account;


    public Order(
        String shipTo,        int number,        float total,        String status,        boolean shipped,        LocalDate ordered    ) {
        this.shipTo = shipTo;
        this.number = number;
        this.total = total;
        this.status = status;
        this.shipped = shipped;
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
    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
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

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }

}