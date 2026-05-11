





import java.util.List;
import java.util.ArrayList;

public class iotdsl_NodeInstance  {

    private String name;





    private iotdsl_Type iotdsl_type;




    private iotdsl_Configuration iotdsl_configuration;


    public iotdsl_NodeInstance(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iotdsl_Type getIotdsl_type() {
        return iotdsl_type;
    }

    public void setIotdsl_type(iotdsl_Type iotdsl_type) {
        this.iotdsl_type = iotdsl_type;
    }
    public iotdsl_Configuration getIotdsl_configuration() {
        return iotdsl_configuration;
    }

    public void setIotdsl_configuration(iotdsl_Configuration iotdsl_configuration) {
        this.iotdsl_configuration = iotdsl_configuration;
    }

}