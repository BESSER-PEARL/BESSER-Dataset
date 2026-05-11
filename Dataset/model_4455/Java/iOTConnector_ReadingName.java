





import java.util.List;
import java.util.ArrayList;

public class iOTConnector_ReadingName  {

    private String name;





    private iOTConnector_Output iotconnector_output;


    public iOTConnector_ReadingName(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public iOTConnector_Output getIotconnector_output() {
        return iotconnector_output;
    }

    public void setIotconnector_output(iOTConnector_Output iotconnector_output) {
        this.iotconnector_output = iotconnector_output;
    }

}