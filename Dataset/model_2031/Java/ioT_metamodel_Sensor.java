





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Sensor extends Device {

    private String Name;
    private boolean State;
    private float frequency;





    private ioT_metamodel_DeviceState iot_metamodel_devicestate;




    private List<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings;


    public ioT_metamodel_Sensor(
        String Name,        boolean State,        float frequency    ) {
        super(
        );
        this.Name = Name;
        this.State = State;
        this.frequency = frequency;
        this.iot_metamodel_physicalthings = new ArrayList<>();
    }

    public ioT_metamodel_Sensor(
        String Name,        boolean State,        float frequency        ArrayList<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings    ) {
        this.Name = Name;
        this.State = State;
        this.frequency = frequency;
        this.iot_metamodel_physicalthings = iot_metamodel_physicalthings;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public boolean getState() {
        return State;
    }

    public void setState(boolean State) {
        this.State = State;
    }
    public float getFrequency() {
        return frequency;
    }

    public void setFrequency(float frequency) {
        this.frequency = frequency;
    }

    public ioT_metamodel_DeviceState getIot_metamodel_devicestate() {
        return iot_metamodel_devicestate;
    }

    public void setIot_metamodel_devicestate(ioT_metamodel_DeviceState iot_metamodel_devicestate) {
        this.iot_metamodel_devicestate = iot_metamodel_devicestate;
    }
    public List<ioT_metamodel_PhysicalThing> getIot_metamodel_physicalthings() {
        return iot_metamodel_physicalthings;
    }

    public void addIot_metamodel_physicalthing(Iot_metamodel_physicalthing iot_metamodel_physicalthing) {
        this.iot_metamodel_physicalthings.add(iot_metamodel_physicalthing);
    }

}