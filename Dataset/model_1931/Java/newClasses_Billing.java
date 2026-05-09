





import java.util.List;
import java.util.ArrayList;

public class newClasses_Billing extends Biller, GuestBiller, CustomerProvides {

    private String totalCost;
    private String isPaid;



    public newClasses_Billing(
        String totalCost,        String isPaid    ) {
        super(
        );
        this.totalCost = totalCost;
        this.isPaid = isPaid;
    }


    public String getTotalcost() {
        return totalCost;
    }

    public void setTotalcost(String totalCost) {
        this.totalCost = totalCost;
    }
    public String getIspaid() {
        return isPaid;
    }

    public void setIspaid(String isPaid) {
        this.isPaid = isPaid;
    }


}