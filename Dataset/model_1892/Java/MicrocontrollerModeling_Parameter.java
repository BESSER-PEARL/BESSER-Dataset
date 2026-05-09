





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_Parameter  {

    private String type;
    private String name;





    private MicrocontrollerModeling_Function microcontrollermodeling_function;


    public MicrocontrollerModeling_Parameter(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public MicrocontrollerModeling_Function getMicrocontrollermodeling_function() {
        return microcontrollermodeling_function;
    }

    public void setMicrocontrollermodeling_function(MicrocontrollerModeling_Function microcontrollermodeling_function) {
        this.microcontrollermodeling_function = microcontrollermodeling_function;
    }

}