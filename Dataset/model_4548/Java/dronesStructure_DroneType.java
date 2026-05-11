





import java.util.List;
import java.util.ArrayList;

public class dronesStructure_DroneType extends NamedElement {

    private float maxBatteryCapacity;
    private float weight;
    private float idleEneryConsumption;





    private dronesStructure_DronesStructure dronesstructure_dronesstructure;


    public dronesStructure_DroneType(
        float maxBatteryCapacity,        float weight,        float idleEneryConsumption    ) {
        super(
        );
        this.maxBatteryCapacity = maxBatteryCapacity;
        this.weight = weight;
        this.idleEneryConsumption = idleEneryConsumption;
    }


    public float getMaxbatterycapacity() {
        return maxBatteryCapacity;
    }

    public void setMaxbatterycapacity(float maxBatteryCapacity) {
        this.maxBatteryCapacity = maxBatteryCapacity;
    }
    public float getWeight() {
        return weight;
    }

    public void setWeight(float weight) {
        this.weight = weight;
    }
    public float getIdleeneryconsumption() {
        return idleEneryConsumption;
    }

    public void setIdleeneryconsumption(float idleEneryConsumption) {
        this.idleEneryConsumption = idleEneryConsumption;
    }

    public dronesStructure_DronesStructure getDronesstructure_dronesstructure() {
        return dronesstructure_dronesstructure;
    }

    public void setDronesstructure_dronesstructure(dronesStructure_DronesStructure dronesstructure_dronesstructure) {
        this.dronesstructure_dronesstructure = dronesstructure_dronesstructure;
    }

}