




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class cliente  {

    private String details;
    private float total;
    private LocalDate paidDate;



    public cliente(
        String details,        float total,        LocalDate paidDate    ) {
        this.details = details;
        this.total = total;
        this.paidDate = paidDate;
    }


    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
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


}