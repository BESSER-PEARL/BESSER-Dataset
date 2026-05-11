





import java.util.List;
import java.util.ArrayList;

public class pycom_ModuleType  {

    private String typeName;
    private String name;





    private pycom_Sensor pycom_sensor;




    private pycom_Actuator pycom_actuator;


    public pycom_ModuleType(
        String typeName,        String name    ) {
        this.typeName = typeName;
        this.name = name;
    }


    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pycom_Sensor getPycom_sensor() {
        return pycom_sensor;
    }

    public void setPycom_sensor(pycom_Sensor pycom_sensor) {
        this.pycom_sensor = pycom_sensor;
    }
    public pycom_Actuator getPycom_actuator() {
        return pycom_actuator;
    }

    public void setPycom_actuator(pycom_Actuator pycom_actuator) {
        this.pycom_actuator = pycom_actuator;
    }

}