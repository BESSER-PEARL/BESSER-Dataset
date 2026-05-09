





import java.util.List;
import java.util.ArrayList;

public class eTJ_Credit extends AccountAttribute {

    private String description;
    private float amount;



    public eTJ_Credit(
        String description,        float amount    ) {
        super(
        );
        this.description = description;
        this.amount = amount;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public float getAmount() {
        return amount;
    }

    public void setAmount(float amount) {
        this.amount = amount;
    }


}