





import java.util.List;
import java.util.ArrayList;

public class Redis  {






    private List<Payment> payments;




    private RedisStateStore redisstatestore;




    private ShoppingCart shoppingcart;


    public Redis(
    ) {
        this.payments = new ArrayList<>();
    }

    public Redis(
        ArrayList<Payment> payments    ) {
        this.payments = payments;
    }


    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }
    public RedisStateStore getRedisstatestore() {
        return redisstatestore;
    }

    public void setRedisstatestore(RedisStateStore redisstatestore) {
        this.redisstatestore = redisstatestore;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}