





import java.util.List;
import java.util.ArrayList;

public class metamodel_Sensor  {

    private String sensorName;
    private String name;



    public metamodel_Sensor(
        String sensorName,        String name    ) {
        this.sensorName = sensorName;
        this.name = name;
    }


    public String getSensorname() {
        return sensorName;
    }

    public void setSensorname(String sensorName) {
        this.sensorName = sensorName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}