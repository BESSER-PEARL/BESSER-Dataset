





import java.util.List;
import java.util.ArrayList;

public class drone_Battery extends NamedElement {

    private float voltage;
    private String cellType;
    private int rechargeTime;
    private int capacity;





    private drone_Drone drone_drone;


    public drone_Battery(
        float voltage,        String cellType,        int rechargeTime,        int capacity    ) {
        super(
        );
        this.voltage = voltage;
        this.cellType = cellType;
        this.rechargeTime = rechargeTime;
        this.capacity = capacity;
    }


    public float getVoltage() {
        return voltage;
    }

    public void setVoltage(float voltage) {
        this.voltage = voltage;
    }
    public String getCelltype() {
        return cellType;
    }

    public void setCelltype(String cellType) {
        this.cellType = cellType;
    }
    public int getRechargetime() {
        return rechargeTime;
    }

    public void setRechargetime(int rechargeTime) {
        this.rechargeTime = rechargeTime;
    }
    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        this.capacity = capacity;
    }

    public drone_Drone getDrone_drone() {
        return drone_drone;
    }

    public void setDrone_drone(drone_Drone drone_drone) {
        this.drone_drone = drone_drone;
    }

}