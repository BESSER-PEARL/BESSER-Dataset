





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_Config  {

    private String name;





    private iOTConnector_Program iotconnector_program;


    public iOTConnector_Config(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iOTConnector_Program getIotconnector_program() {
        return iotconnector_program;
    }

    public void setIotconnector_program(iOTConnector_Program iotconnector_program) {
        this.iotconnector_program = iotconnector_program;
    }

}