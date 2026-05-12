




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String shipTo;
    private int number;
    private float total;
    private boolean shipped;
    private LocalDate ordered;
    private None status;





    private ShoppingCart1 shoppingcart1;




    private Payment payment;


    public Order(
        String shipTo,        int number,        float total,        boolean shipped,        LocalDate ordered,        None status    ) {
        this.shipTo = shipTo;
        this.number = number;
        this.total = total;
        this.shipped = shipped;
        this.ordered = ordered;
        this.status = status;
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

    public ShoppingCart1 getShoppingcart1() {
        return shoppingcart1;
    }

    public void setShoppingcart1(ShoppingCart1 shoppingcart1) {
        this.shoppingcart1 = shoppingcart1;
    }
    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }

}