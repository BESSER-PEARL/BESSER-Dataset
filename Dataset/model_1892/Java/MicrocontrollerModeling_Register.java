





import java.util.List;
import java.util.ArrayList;

public class MicrocontrollerModeling_Register  {

    private String name;
    private String type;





    private MicrocontrollerModeling_Microcontroller microcontrollermodeling_microcontroller;


    public MicrocontrollerModeling_Register(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
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

    public MicrocontrollerModeling_Microcontroller getMicrocontrollermodeling_microcontroller() {
        return microcontrollermodeling_microcontroller;
    }

    public void setMicrocontrollermodeling_microcontroller(MicrocontrollerModeling_Microcontroller microcontrollermodeling_microcontroller) {
        this.microcontrollermodeling_microcontroller = microcontrollermodeling_microcontroller;
    }

}