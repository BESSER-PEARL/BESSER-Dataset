





import java.util.List;
import java.util.ArrayList;

public class project_Credit extends AccountAttribute {

    private String date;
    private String description;
    private float amount;



    public project_Credit(
        String date,        String description,        float amount    ) {
        super(
        );
        this.date = date;
        this.description = description;
        this.amount = amount;
    }


    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
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