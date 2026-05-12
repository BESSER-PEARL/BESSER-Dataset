





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String createdAt;
    private int id;
    private int amount;





    private Buyer buyer;


    public Order(
        String createdAt,        int id,        int amount    ) {
        this.createdAt = createdAt;
        this.id = id;
        this.amount = amount;
    }


    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
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