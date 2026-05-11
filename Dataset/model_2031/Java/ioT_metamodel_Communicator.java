





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Communicator  {

    private String Type;
    private int ports_number;





    private ioT_metamodel_Device iot_metamodel_device;


    public ioT_metamodel_Communicator(
        String Type,        int ports_number    ) {
        this.Type = Type;
        this.ports_number = ports_number;
    }


    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }
    public int getPorts_number() {
        return ports_number;
    }

    public void setPorts_number(int ports_number) {
        this.ports_number = ports_number;
    }

    public ioT_metamodel_Device getIot_metamodel_device() {
        return iot_metamodel_device;
    }

    public void setIot_metamodel_device(ioT_metamodel_Device iot_metamodel_device) {
        this.iot_metamodel_device = iot_metamodel_device;
    }

}