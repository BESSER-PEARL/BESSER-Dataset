




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private LocalDate paidDate;
    private float total;
    private String details;



    public Payment(
        LocalDate paidDate,        float total,        String details    ) {
        this.paidDate = paidDate;
        this.total = total;
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
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }


}