





import java.util.List;
import java.util.ArrayList;

public class device_Types  {






    private List<device_Device> device_devices;


    public device_Types(
    ) {
        this.device_devices = new ArrayList<>();
    }

    public device_Types(
        ArrayList<device_Device> device_devices    ) {
        this.device_devices = device_devices;
    }


    public List<device_Device> getDevice_devices() {
        return device_devices;
    }

    public void addDevice_device(Device_device device_device) {
        this.device_devices.add(device_device);
    }

}