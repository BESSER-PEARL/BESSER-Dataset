





import java.util.List;
import java.util.ArrayList;

public class iotdsl_Parameter  {

    private String name;





    private iotdsl_Capability iotdsl_capability;




    private iotdsl_Type iotdsl_type;


    public iotdsl_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iotdsl_Capability getIotdsl_capability() {
        return iotdsl_capability;
    }

    public void setIotdsl_capability(iotdsl_Capability iotdsl_capability) {
        this.iotdsl_capability = iotdsl_capability;
    }
    public iotdsl_Type getIotdsl_type() {
        return iotdsl_type;
    }

    public void setIotdsl_type(iotdsl_Type iotdsl_type) {
        this.iotdsl_type = iotdsl_type;
    }

}