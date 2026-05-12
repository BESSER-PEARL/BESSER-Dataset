





import java.util.List;
import java.util.ArrayList;

public class driver_TransferToSymbian  {

    private String group;





    private driver_Task driver_task;




    private List<driver_Transfer> driver_transfers;


    public driver_TransferToSymbian(
        String group    ) {
        this.group = group;
        this.driver_transfers = new ArrayList<>();
    }

    public driver_TransferToSymbian(
        String group        ArrayList<driver_Transfer> driver_transfers    ) {
        this.group = group;
        this.driver_transfers = driver_transfers;
    }

    public String getGroup() {
        return group;
    }

    public void setGroup(String group) {
        this.group = group;
    }

    public driver_Task getDriver_task() {
        return driver_task;
    }

    public void setDriver_task(driver_Task driver_task) {
        this.driver_task = driver_task;
    }
    public List<driver_Transfer> getDriver_transfers() {
        return driver_transfers;
    }

    public void addDriver_transfer(Driver_transfer driver_transfer) {
        this.driver_transfers.add(driver_transfer);
    }

}