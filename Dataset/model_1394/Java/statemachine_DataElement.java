





import java.util.List;
import java.util.ArrayList;

public class statemachine_DataElement  {

    private String ioType;
    private int port;
    private String name;





    private statemachine_Statechart statemachine_statechart;


    public statemachine_DataElement(
        String ioType,        int port,        String name    ) {
        this.ioType = ioType;
        this.port = port;
        this.name = name;
    }


    public String getIotype() {
        return ioType;
    }

    public void setIotype(String ioType) {
        this.ioType = ioType;
    }
    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statemachine_Statechart getStatemachine_statechart() {
        return statemachine_statechart;
    }

    public void setStatemachine_statechart(statemachine_Statechart statemachine_statechart) {
        this.statemachine_statechart = statemachine_statechart;
    }

}