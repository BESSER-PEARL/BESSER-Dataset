





import java.util.List;
import java.util.ArrayList;

public class ioT_VarOrList  {

    private String name;





    private ioT_Program iot_program;


    public ioT_VarOrList(
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

}