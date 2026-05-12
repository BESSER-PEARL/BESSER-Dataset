





import java.util.List;
import java.util.ArrayList;

public class Order  {

    private String createdAt;
    private int amount;
    private int id;





    private Buyer buyer;


    public Order(
        String createdAt,        int amount,        int id    ) {
        this.createdAt = createdAt;
        this.amount = amount;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Buyer getBuyer() {
        return buyer;
    }

    public void setBuyer(Buyer buyer) {
        this.buyer = buyer;
    }

}