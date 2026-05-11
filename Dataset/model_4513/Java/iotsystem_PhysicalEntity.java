





import java.util.List;
import java.util.ArrayList;

public class iotsystem_PhysicalEntity extends NamedElement {






    private iotsystem_IotSystem iotsystem_iotsystem;




    private List<iotsystem_Device> iotsystem_devices;


    public iotsystem_PhysicalEntity(
    ) {
        super(
        );
        this.iotsystem_devices = new ArrayList<>();
    }

    public iotsystem_PhysicalEntity(
        ArrayList<iotsystem_Device> iotsystem_devices    ) {
        this.iotsystem_devices = iotsystem_devices;
    }


    public iotsystem_IotSystem getIotsystem_iotsystem() {
        return iotsystem_iotsystem;
    }

    public void setIotsystem_iotsystem(iotsystem_IotSystem iotsystem_iotsystem) {
        this.iotsystem_iotsystem = iotsystem_iotsystem;
    }
    public List<iotsystem_Device> getIotsystem_devices() {
        return iotsystem_devices;
    }

    public void addIotsystem_device(Iotsystem_device iotsystem_device) {
        this.iotsystem_devices.add(iotsystem_device);
    }

}