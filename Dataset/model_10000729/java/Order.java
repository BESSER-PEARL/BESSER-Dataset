





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private int id;
    private String createdAt;
    private int amount;





    private Buyer buyer;


    public Order(
        int id,        String createdAt,        int amount    ) {
        this.id = id;
        this.createdAt = createdAt;
        this.amount = amount;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public int getAmount() {
        return amount;
    }

    public void setAmount(int amount) {
        this.amount = amount;
    }

    public Buyer getBuyer() {
        return buyer;
    }

    public void setBuyer(Buyer buyer) {
        this.buyer = buyer;
    }

}