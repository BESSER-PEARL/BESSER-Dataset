





import java.util.List;
import java.util.ArrayList;

public class iotw_Mainboard  {

    private String name;





    private iotw_Device iotw_device;




    private List<iotw_Device> iotw_devices;


    public iotw_Mainboard(
        String name    ) {
        this.name = name;
        this.iotw_devices = new ArrayList<>();
    }

    public iotw_Mainboard(
        String name        ArrayList<iotw_Device> iotw_devices    ) {
        this.name = name;
        this.iotw_devices = iotw_devices;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iotw_Device getIotw_device() {
        return iotw_device;
    }

    public void setIotw_device(iotw_Device iotw_device) {
        this.iotw_device = iotw_device;
    }
    public List<iotw_Device> getIotw_devices() {
        return iotw_devices;
    }

    public void addIotw_device(Iotw_device iotw_device) {
        this.iotw_devices.add(iotw_device);
    }

}