





import java.util.List;
import java.util.ArrayList;

public class transaction_Transaction  {

    private float amount;
    private None type;
    private int id;



    public transaction_Transaction(
        float amount,        None type,        int id    ) {
        this.amount = amount;
        this.type = type;
        this.id = id;
    }


    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public None getType() {
        return type;
    }

    public void setType(None type) {
        this.type = type;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}