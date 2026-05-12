





import java.util.List;
import java.util.ArrayList;

public class Redis  {






    private RedisClient redisclient;




    private List<Payment> payments;




    private ShoppingCart shoppingcart;


    public Redis(
    ) {
        this.payments = new ArrayList<>();
    }

    public Redis(
        ArrayList<Payment> payments    ) {
        this.payments = payments;
    }


    public RedisClient getRedisclient() {
        return redisclient;
    }

    public void setRedisclient(RedisClient redisclient) {
        this.redisclient = redisclient;
    }
    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}