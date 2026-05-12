




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private float total;
    private LocalDate paidDate;
    private String details;



    public Payment(
        float total,        LocalDate paidDate,        String details    ) {
        this.total = total;
        this.paidDate = paidDate;
        this.details = details;
    }


    public float getTotal() {
        return total;
    }

    public void setTotal(float total) {
        this.total = total;
    }
    public LocalDate getPaiddate() {
        return paidDate;
    }

    public void setPaiddate(LocalDate paidDate) {
        this.paidDate = paidDate;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }


}