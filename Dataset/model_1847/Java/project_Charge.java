





import java.util.List;
import java.util.ArrayList;

public class project_Charge extends TaskAttribute {

    private float amount;
    private String applies;



    public project_Charge(
        float amount,        String applies    ) {
        super(
        );
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