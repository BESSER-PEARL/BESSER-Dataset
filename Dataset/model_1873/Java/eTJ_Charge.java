





import java.util.List;
import java.util.ArrayList;

public class eTJ_Charge  {

    private float amount;
    private String applies;



    public eTJ_Charge(
        float amount,        String applies    ) {
        this.amount = amount;
        this.applies = applies;
    }


    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }
    public String getApplies() {
        return applies;
    }

    public void setApplies(String applies) {
        this.applies = applies;
    }


}