




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private String details;
    private LocalDate paidDate;
    private float total;



    public Payment(
        String details,        LocalDate paidDate,        float total    ) {
        this.details = details;
        this.paidDate = paidDate;
        this.total = total;
    }


    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }
    public LocalDate getPaiddate() {
        return paidDate;
    }

    public void setPaiddate(LocalDate paidDate) {
        this.paidDate = paidDate;
    }
    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }


}