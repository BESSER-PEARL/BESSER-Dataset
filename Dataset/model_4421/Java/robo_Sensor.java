





import java.util.List;
import java.util.ArrayList;

public class robo_Sensor  {

    private String port;
    private String mode;
    private String name;
    private String type;



    public robo_Sensor(
        String port,        String mode,        String name,        String type    ) {
        this.port = port;
        this.mode = mode;
        this.name = name;
        this.type = type;
    }


    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
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


}