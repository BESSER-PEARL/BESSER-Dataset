





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_Sensor  {

    private String name;
    private String type;





    private iOTConnector_Config iotconnector_config;




    private List<iOTConnector_Function> iotconnector_functions;


    public iOTConnector_Sensor(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
        this.iotconnector_functions = new ArrayList<>();
    }

    public iOTConnector_Sensor(
        String name,        String type        ArrayList<iOTConnector_Function> iotconnector_functions    ) {
        this.name = name;
        this.type = type;
        this.iotconnector_functions = iotconnector_functions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public iOTConnector_Config getIotconnector_config() {
        return iotconnector_config;
    }

    public void setIotconnector_config(iOTConnector_Config iotconnector_config) {
        this.iotconnector_config = iotconnector_config;
    }
    public List<iOTConnector_Function> getIotconnector_functions() {
        return iotconnector_functions;
    }

    public void addIotconnector_function(Iotconnector_function iotconnector_function) {
        this.iotconnector_functions.add(iotconnector_function);
    }

}