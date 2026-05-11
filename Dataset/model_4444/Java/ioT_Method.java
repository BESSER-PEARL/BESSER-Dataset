





import java.util.List;
import java.util.ArrayList;

public class ioT_Method  {

    private String parameters;
    private String name;





    private ioT_SensorGetMethod iot_sensorgetmethod;


    public ioT_Method(
        String parameters,        String name    ) {
        this.parameters = parameters;
        this.name = name;
    }


    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioT_SensorGetMethod getIot_sensorgetmethod() {
        return iot_sensorgetmethod;
    }

    public void setIot_sensorgetmethod(ioT_SensorGetMethod iot_sensorgetmethod) {
        this.iot_sensorgetmethod = iot_sensorgetmethod;
    }

}