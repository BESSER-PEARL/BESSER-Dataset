





import java.util.List;
import java.util.ArrayList;

public class payment  {

    private int cardID;
    private int amount;





    private Order order;


    public payment(
        int cardID,        int amount    ) {
        this.cardID = cardID;
        this.amount = amount;
    }


    public int getCardid() {
        return cardID;
    }

    public void setCardid(int cardID) {
        this.cardID = cardID;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}