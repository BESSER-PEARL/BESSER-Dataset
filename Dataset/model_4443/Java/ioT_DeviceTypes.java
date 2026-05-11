





import java.util.List;
import java.util.ArrayList;

public class ioT_DeviceTypes  {






    private List<ioT_DeviceType> iot_devicetypes;


    public ioT_DeviceTypes(
    ) {
        this.iot_devicetypes = new ArrayList<>();
    }

    public ioT_DeviceTypes(
        ArrayList<ioT_DeviceType> iot_devicetypes    ) {
        this.iot_devicetypes = iot_devicetypes;
    }


    public List<ioT_DeviceType> getIot_devicetypes() {
        return iot_devicetypes;
    }

    public void addIot_devicetype(Iot_devicetype iot_devicetype) {
        this.iot_devicetypes.add(iot_devicetype);
    }

}