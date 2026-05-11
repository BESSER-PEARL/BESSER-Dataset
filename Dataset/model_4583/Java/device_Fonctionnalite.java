





import java.util.List;
import java.util.ArrayList;

public class device_Fonctionnalite  {

    private String name;





    private device_Device device_device;


    public device_Fonctionnalite(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public device_Device getDevice_device() {
        return device_device;
    }

    public void setDevice_device(device_Device device_device) {
        this.device_device = device_device;
    }

}