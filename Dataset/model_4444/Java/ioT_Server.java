





import java.util.List;
import java.util.ArrayList;

public class ioT_Server  {

    private String name;





    private ioT_ServerType iot_servertype;


    public ioT_Server(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ioT_ServerType getIot_servertype() {
        return iot_servertype;
    }

    public void setIot_servertype(ioT_ServerType iot_servertype) {
        this.iot_servertype = iot_servertype;
    }

}