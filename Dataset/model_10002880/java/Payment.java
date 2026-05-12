




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Payment  {

    private float total;
    private String details;
    private LocalDate paidDate;





    private Order order;


    public Payment(
        float total,        String details,        LocalDate paidDate    ) {
        this.total = total;
        this.details = details;
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
    public LocalDate getPaiddate() {
        return paidDate;
    }

    public void setPaiddate(LocalDate paidDate) {
        this.paidDate = paidDate;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}