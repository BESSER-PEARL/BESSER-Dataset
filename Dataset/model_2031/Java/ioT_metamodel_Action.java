





import java.util.List;
import java.util.ArrayList;

public class ioT_metamodel_Action  {

    private String Description;





    private ioT_metamodel_DeviceSensor iot_metamodel_devicesensor;




    private ioT_metamodel_Rule iot_metamodel_rule;


    public ioT_metamodel_Action(
        String Description    ) {
        this.Description = Description;
    }


    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }

    public ioT_metamodel_DeviceSensor getIot_metamodel_devicesensor() {
        return iot_metamodel_devicesensor;
    }

    public void setIot_metamodel_devicesensor(ioT_metamodel_DeviceSensor iot_metamodel_devicesensor) {
        this.iot_metamodel_devicesensor = iot_metamodel_devicesensor;
    }
    public ioT_metamodel_Rule getIot_metamodel_rule() {
        return iot_metamodel_rule;
    }

    public void setIot_metamodel_rule(ioT_metamodel_Rule iot_metamodel_rule) {
        this.iot_metamodel_rule = iot_metamodel_rule;
    }

}