





import java.util.List;
import java.util.ArrayList;

public class FSM_State  {

    private boolean isAccepting;
    private String name;



    public FSM_State(
        boolean isAccepting,        String name    ) {
        this.isAccepting = isAccepting;
        this.name = name;
    }


    public boolean getIsaccepting() {
        return isAccepting;
    }

    public void setIsaccepting(boolean isAccepting) {
        this.isAccepting = isAccepting;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}