





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Feature  {

    private String name;





    private iotdsl_Device iotdsl_device;


    public iotdsl_Feature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iotdsl_Device getIotdsl_device() {
        return iotdsl_device;
    }

    public void setIotdsl_device(iotdsl_Device iotdsl_device) {
        this.iotdsl_device = iotdsl_device;
    }

}