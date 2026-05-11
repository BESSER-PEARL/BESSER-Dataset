





import java.util.List;
import java.util.ArrayList;

public class df_Entity extends Attributable, Adaptable {

    private String incomingPortMap;
    private String name;
    private String outgoingPortMap;



    public df_Entity(
        String incomingPortMap,        String name,        String outgoingPortMap    ) {
        super(
        );
        this.incomingPortMap = incomingPortMap;
        this.name = name;
        this.outgoingPortMap = outgoingPortMap;
    }


    public String getIncomingportmap() {
        return incomingPortMap;
    }

    public void setIncomingportmap(String incomingPortMap) {
        this.incomingPortMap = incomingPortMap;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOutgoingportmap() {
        return outgoingPortMap;
    }

    public void setOutgoingportmap(String outgoingPortMap) {
        this.outgoingPortMap = outgoingPortMap;
    }


}