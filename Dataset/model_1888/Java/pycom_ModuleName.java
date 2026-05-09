





import java.util.List;
import java.util.ArrayList;

public class pycom_ModuleName  {

    private String name;





    private pycom_Sensor pycom_sensor;


    public pycom_ModuleName(
        String name    ) {
        this.name = name;
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

}