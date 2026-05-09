





import java.util.List;
import java.util.ArrayList;

public class fsm_FSM  {

    private boolean isServer;
    private String groupId;
    private String name;



    public fsm_FSM(
        boolean isServer,        String groupId,        String name    ) {
        this.isServer = isServer;
        this.groupId = groupId;
        this.name = name;
    }


    public boolean getIsserver() {
        return isServer;
    }

    public void setIsserver(boolean isServer) {
        this.isServer = isServer;
    }
    public String getGroupid() {
        return groupId;
    }

    public void setGroupid(String groupId) {
        this.groupId = groupId;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}