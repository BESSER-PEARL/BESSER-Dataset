





import java.util.List;
import java.util.ArrayList;

public class Basket  {

    private int id;
    private String updatedAt;





    private Buyer buyer;


    public Basket(
        int id,        String updatedAt    ) {
        this.id = id;
        this.updatedAt = updatedAt;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getUpdatedat() {
        return updatedAt;
    }

    public void setUpdatedat(String updatedAt) {
        this.updatedAt = updatedAt;
    }

    public Buyer getBuyer() {
        return buyer;
    }

    public void setBuyer(Buyer buyer) {
        this.buyer = buyer;
    }

}