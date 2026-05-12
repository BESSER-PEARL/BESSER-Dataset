




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String id;
    private LocalDate paid;
    private float total;
    private String details;



    public Payment(
        String id,        LocalDate paid,        float total,        String details    ) {
        this.id = id;
        this.paid = paid;
        this.total = total;
        this.details = details;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public LocalDate getPaid() {
        return paid;
    }

    public void setPaid(LocalDate paid) {
        this.paid = paid;
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


}