





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_Board  {

    private String name;





    private iOTConnector_Program iotconnector_program;




    private iOTConnector_Config iotconnector_config;


    public iOTConnector_Board(
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
    public iOTConnector_Config getIotconnector_config() {
        return iotconnector_config;
    }

    public void setIotconnector_config(iOTConnector_Config iotconnector_config) {
        this.iotconnector_config = iotconnector_config;
    }

}