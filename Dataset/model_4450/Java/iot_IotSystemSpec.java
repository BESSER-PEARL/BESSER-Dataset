





import java.util.List;
import java.util.ArrayList;

public class iot_IotSystemSpec  {

    private String name;





    private iot_IotSystem iot_iotsystem;


    public iot_IotSystemSpec(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iot_IotSystem getIot_iotsystem() {
        return iot_iotsystem;
    }

    public void setIot_iotsystem(iot_IotSystem iot_iotsystem) {
        this.iot_iotsystem = iot_iotsystem;
    }

}