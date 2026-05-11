





import java.util.List;
import java.util.ArrayList;

public class ioT_Device  {

    private String name;





    private ioT_Program iot_program;




    private ioT_Model iot_model;


    public ioT_Device(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioT_Program getIot_program() {
        return iot_program;
    }

    public void setIot_program(ioT_Program iot_program) {
        this.iot_program = iot_program;
    }
    public ioT_Model getIot_model() {
        return iot_model;
    }

    public void setIot_model(ioT_Model iot_model) {
        this.iot_model = iot_model;
    }

}