





import java.util.List;
import java.util.ArrayList;

public class oaam_hardware_HardwareContainerA extends OaamBaseElementA {






    private List<Device> devices;


    public oaam_hardware_HardwareContainerA(
    ) {
        super(
        );
        this.devices = new ArrayList<>();
    }

    public oaam_hardware_HardwareContainerA(
        ArrayList<Device> devices    ) {
        this.devices = devices;
    }


    public List<Device> getDevices() {
        return devices;
    }

    public void addDevice(Device device) {
        this.devices.add(device);
    }

}