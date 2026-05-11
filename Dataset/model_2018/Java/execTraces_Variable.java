





import java.util.List;
import java.util.ArrayList;

public class execTraces_Variable  {

    private String name;





    private execTraces_Node exectraces_node;


    public execTraces_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public execTraces_Node getExectraces_node() {
        return exectraces_node;
    }

    public void setExectraces_node(execTraces_Node exectraces_node) {
        this.exectraces_node = exectraces_node;
    }

}