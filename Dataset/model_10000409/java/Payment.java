




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String id;
    private float total;
    private String details;
    private LocalDate paid;



    public Payment(
        String id,        float total,        String details,        LocalDate paid    ) {
        this.id = id;
        this.total = total;
        this.details = details;
        this.paid = paid;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }
    public LocalDate getPaid() {
        return paid;
    }

    public void setPaid(LocalDate paid) {
        this.paid = paid;
    }


}