





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_DeviceState  {

    private boolean Enabled;





    private ioT_metamodel_Device iot_metamodel_device;


    public ioT_metamodel_DeviceState(
        boolean Enabled    ) {
        this.Enabled = Enabled;
    }


    public boolean getEnabled() {
        return Enabled;
    }

    public void setEnabled(boolean Enabled) {
        this.Enabled = Enabled;
    }

    public ioT_metamodel_Device getIot_metamodel_device() {
        return iot_metamodel_device;
    }

    public void setIot_metamodel_device(ioT_metamodel_Device iot_metamodel_device) {
        this.iot_metamodel_device = iot_metamodel_device;
    }

}