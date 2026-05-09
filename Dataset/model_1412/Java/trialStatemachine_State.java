





import java.util.List;
import java.util.ArrayList;

public class trialStatemachine_State  {

    private String name;
    private String initialState;



    public trialStatemachine_State(
        String name,        String initialState    ) {
        this.name = name;
        this.initialState = initialState;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInitialstate() {
        return initialState;
    }

    public void setInitialstate(String initialState) {
        this.initialState = initialState;
    }


}