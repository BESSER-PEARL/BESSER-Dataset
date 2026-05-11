





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Actuator extends Device {

    private String name;





    private ioT_metamodel_DeviceState iot_metamodel_devicestate;




    private List<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings;


    public ioT_metamodel_Actuator(
        String name    ) {
        super(
        );
        this.name = name;
        this.iot_metamodel_physicalthings = new ArrayList<>();
    }

    public ioT_metamodel_Actuator(
        String name        ArrayList<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings    ) {
        this.name = name;
        this.iot_metamodel_physicalthings = iot_metamodel_physicalthings;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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