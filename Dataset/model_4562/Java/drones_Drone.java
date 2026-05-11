





import java.util.List;
import java.util.ArrayList;

public class drones_Drone extends SizedElement, NamedElement {

    private float maxSpeed;
    private float maxPayload;
    private float minSpeed;
    private float communicationRange;
    private int cpuFrequency;
    private int memory;





    private List<drones_Action> drones_actions;


    public drones_Drone(
        float maxSpeed,        float maxPayload,        float minSpeed,        float communicationRange,        int cpuFrequency,        int memory    ) {
        super(
        );
        this.maxSpeed = maxSpeed;
        this.maxPayload = maxPayload;
        this.minSpeed = minSpeed;
        this.communicationRange = communicationRange;
        this.cpuFrequency = cpuFrequency;
        this.memory = memory;
        this.drones_actions = new ArrayList<>();
    }

    public drones_Drone(
        float maxSpeed,        float maxPayload,        float minSpeed,        float communicationRange,        int cpuFrequency,        int memory        ArrayList<drones_Action> drones_actions    ) {
        this.maxSpeed = maxSpeed;
        this.maxPayload = maxPayload;
        this.minSpeed = minSpeed;
        this.communicationRange = communicationRange;
        this.cpuFrequency = cpuFrequency;
        this.memory = memory;
        this.drones_actions = drones_actions;
    }

    public float getMaxspeed() {
        return maxSpeed;
    }

    public void setMaxspeed(float maxSpeed) {
        this.maxSpeed = maxSpeed;
    }
    public float getMaxpayload() {
        return maxPayload;
    }

    public void setMaxpayload(float maxPayload) {
        this.maxPayload = maxPayload;
    }
    public float getMinspeed() {
        return minSpeed;
    }

    public void setMinspeed(float minSpeed) {
        this.minSpeed = minSpeed;
    }
    public float getCommunicationrange() {
        return communicationRange;
    }

    public void setCommunicationrange(float communicationRange) {
        this.communicationRange = communicationRange;
    }
    public int getCpufrequency() {
        return cpuFrequency;
    }

    public void setCpufrequency(int cpuFrequency) {
        this.cpuFrequency = cpuFrequency;
    }
    public int getMemory() {
        return memory;
    }

    public void setMemory(int memory) {
        this.memory = memory;
    }

    public List<drones_Action> getDrones_actions() {
        return drones_actions;
    }

    public void addDrones_action(Drones_action drones_action) {
        this.drones_actions.add(drones_action);
    }

}