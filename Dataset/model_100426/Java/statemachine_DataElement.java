





import java.util.List;
import java.util.ArrayList;

public class statemachine_DataElement  {

    private int port;
    private String ioType;
    private String name;



    public statemachine_DataElement(
        int port,        String ioType,        String name    ) {
        this.port = port;
        this.ioType = ioType;
        this.name = name;
    }


    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getIotype() {
        return ioType;
    }

    public void setIotype(String ioType) {
        this.ioType = ioType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}