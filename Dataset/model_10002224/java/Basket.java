





import java.util.List;
import java.util.ArrayList;

public class Basket  {

    private String updatedAt;
    private int id;





    private Buyer buyer;


    public Basket(
        String updatedAt,        int id    ) {
        this.updatedAt = updatedAt;
        this.id = id;
    }


    public String getUpdatedat() {
        return updatedAt;
    }

    public void setUpdatedat(String updatedAt) {
        this.updatedAt = updatedAt;
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