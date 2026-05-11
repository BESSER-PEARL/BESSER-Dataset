





import java.util.List;
import java.util.ArrayList;

public class adfg_AperiodicActor extends Actor {

    private String replenishmentPeriod;
    private String capacity;



    public adfg_AperiodicActor(
        String replenishmentPeriod,        String capacity    ) {
        super(
        );
        this.replenishmentPeriod = replenishmentPeriod;
        this.capacity = capacity;
    }


    public String getReplenishmentperiod() {
        return replenishmentPeriod;
    }

    public void setReplenishmentperiod(String replenishmentPeriod) {
        this.replenishmentPeriod = replenishmentPeriod;
    }
    public String getCapacity() {
        return capacity;
    }

    public void setCapacity(String capacity) {
        this.capacity = capacity;
    }


}