





import java.util.List;
import java.util.ArrayList;

public class FSM_StateMachine  {

    private String name;
    private String genBy;



    public FSM_StateMachine(
        String name,        String genBy    ) {
        this.name = name;
        this.genBy = genBy;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getGenby() {
        return genBy;
    }

    public void setGenby(String genBy) {
        this.genBy = genBy;
    }


}