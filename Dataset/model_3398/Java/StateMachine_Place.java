





import java.util.List;
import java.util.ArrayList;

public class StateMachine_Place  {

    private String name;
    private int tokens;



    public StateMachine_Place(
        String name,        int tokens    ) {
        this.name = name;
        this.tokens = tokens;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getTokens() {
        return tokens;
    }

    public void setTokens(int tokens) {
        this.tokens = tokens;
    }


}