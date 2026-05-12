





import java.util.List;
import java.util.ArrayList;

public class Transaction  {

    private int shipmentNumber;
    private int orderId;





    private Card card;


    public Transaction(
        int shipmentNumber,        int orderId    ) {
        this.shipmentNumber = shipmentNumber;
        this.orderId = orderId;
    }


    public int getShipmentnumber() {
        return shipmentNumber;
    }

    public void setShipmentnumber(int shipmentNumber) {
        this.shipmentNumber = shipmentNumber;
    }
    public int getOrderid() {
        return orderId;
    }

    public void setOrderid(int orderId) {
        this.orderId = orderId;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }

}