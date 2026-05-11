





import java.util.List;
import java.util.ArrayList;

public class drones_Battery extends TemporalContainmentProxy {

    private float charge;
    private float remainingLifeTime;
    private float rechargeRate;
    private float lifeTime;





    private drones_Drone drones_drone;


    public drones_Battery(
        float charge,        float remainingLifeTime,        float rechargeRate,        float lifeTime    ) {
        super(
        );
        this.charge = charge;
        this.remainingLifeTime = remainingLifeTime;
        this.rechargeRate = rechargeRate;
        this.lifeTime = lifeTime;
    }


    public float getCharge() {
        return charge;
    }

    public void setCharge(float charge) {
        this.charge = charge;
    }
    public float getRemaininglifetime() {
        return remainingLifeTime;
    }

    public void setRemaininglifetime(float remainingLifeTime) {
        this.remainingLifeTime = remainingLifeTime;
    }
    public float getRechargerate() {
        return rechargeRate;
    }

    public void setRechargerate(float rechargeRate) {
        this.rechargeRate = rechargeRate;
    }
    public float getLifetime() {
        return lifeTime;
    }

    public void setLifetime(float lifeTime) {
        this.lifeTime = lifeTime;
    }

    public drones_Drone getDrones_drone() {
        return drones_drone;
    }

    public void setDrones_drone(drones_Drone drones_drone) {
        this.drones_drone = drones_drone;
    }

}