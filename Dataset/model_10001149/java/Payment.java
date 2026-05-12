





import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String Amount;





    private Order order;


    public Payment(
        String Amount    ) {
        this.Amount = Amount;
    }


    public String getAmount() {
        return Amount;
    }

    public void setAmount(String Amount) {
        this.Amount = Amount;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}