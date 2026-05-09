





import java.util.List;
import java.util.ArrayList;

public class oaam_allocations_Message extends MessageA {






    private Bus bus;




    private List<Device> devices;




    private MessageOnBusCapability messageonbuscapability;




    private List<Device> devices;


    public oaam_allocations_Message(
    ) {
        super(
        );
        this.devices = new ArrayList<>();
        this.devices = new ArrayList<>();
    }

    public oaam_allocations_Message(
        ArrayList<Device> devices,        ArrayList<Device> devices    ) {
        this.devices = devices;
        this.devices = devices;
    }


    public Bus getBus() {
        return bus;
    }

    public void setBus(Bus bus) {
        this.bus = bus;
    }
    public List<Device> getDevices() {
        return devices;
    }

    public void addDevice(Device device) {
        this.devices.add(device);
    }
    public MessageOnBusCapability getMessageonbuscapability() {
        return messageonbuscapability;
    }

    public void setMessageonbuscapability(MessageOnBusCapability messageonbuscapability) {
        this.messageonbuscapability = messageonbuscapability;
    }
    public List<Device> getDevices() {
        return devices;
    }

    public void addDevice(Device device) {
        this.devices.add(device);
    }

}