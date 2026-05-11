





import java.util.List;
import java.util.ArrayList;

public class amazoninformational_Order  {

    private String status;
    private float totalAmount;



    public amazoninformational_Order(
        String status,        float totalAmount    ) {
        this.status = status;
        this.totalAmount = totalAmount;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public float getTotalamount() {
        return totalAmount;
    }

    public void setTotalamount(float totalAmount) {
        this.totalAmount = totalAmount;
    }


}