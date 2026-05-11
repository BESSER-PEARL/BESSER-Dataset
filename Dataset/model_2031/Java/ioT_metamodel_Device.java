





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Device extends PhysicalThing {

    private String Technology;





    private ioT_metamodel_PhysicalThing iot_metamodel_physicalthing;




    private List<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings;




    private List<ioT_metamodel_Device> iot_metamodel_devices;


    public ioT_metamodel_Device(
        String Technology    ) {
        super(
        );
        this.Technology = Technology;
        this.iot_metamodel_physicalthings = new ArrayList<>();
        this.iot_metamodel_devices = new ArrayList<>();
    }

    public ioT_metamodel_Device(
        String Technology        ArrayList<ioT_metamodel_PhysicalThing> iot_metamodel_physicalthings,        ArrayList<ioT_metamodel_Device> iot_metamodel_devices    ) {
        this.Technology = Technology;
        this.iot_metamodel_physicalthings = iot_metamodel_physicalthings;
        this.iot_metamodel_devices = iot_metamodel_devices;
    }

    public String getTechnology() {
        return Technology;
    }

    public void setTechnology(String Technology) {
        this.Technology = Technology;
    }

    public ioT_metamodel_PhysicalThing getIot_metamodel_physicalthing() {
        return iot_metamodel_physicalthing;
    }

    public void setIot_metamodel_physicalthing(ioT_metamodel_PhysicalThing iot_metamodel_physicalthing) {
        this.iot_metamodel_physicalthing = iot_metamodel_physicalthing;
    }
    public List<ioT_metamodel_PhysicalThing> getIot_metamodel_physicalthings() {
        return iot_metamodel_physicalthings;
    }

    public void addIot_metamodel_physicalthing(Iot_metamodel_physicalthing iot_metamodel_physicalthing) {
        this.iot_metamodel_physicalthings.add(iot_metamodel_physicalthing);
    }
    public List<ioT_metamodel_Device> getIot_metamodel_devices() {
        return iot_metamodel_devices;
    }

    public void addIot_metamodel_device(Iot_metamodel_device iot_metamodel_device) {
        this.iot_metamodel_devices.add(iot_metamodel_device);
    }

}