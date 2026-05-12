





import java.util.List;
import java.util.ArrayList;

public class transacao_transacao  {

    private String type;
    private int id;
    private float amount;



    public transacao_transacao(
        String type,        int id,        float amount    ) {
        this.type = type;
        this.id = id;
        this.amount = amount;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }


}