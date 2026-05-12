





import java.util.List;
import java.util.ArrayList;

public class statespace_Transition extends Storage {

    private int match;
    private int parameterCount;
    private String parameterKeys;



    public statespace_Transition(
        int match,        int parameterCount,        String parameterKeys    ) {
        super(
        );
        this.match = match;
        this.parameterCount = parameterCount;
        this.parameterKeys = parameterKeys;
    }


    public int getMatch() {
        return match;
    }

    public void setMatch(int match) {
        this.match = match;
    }
    public int getParametercount() {
        return parameterCount;
    }

    public void setParametercount(int parameterCount) {
        this.parameterCount = parameterCount;
    }
    public String getParameterkeys() {
        return parameterKeys;
    }

    public void setParameterkeys(String parameterKeys) {
        this.parameterKeys = parameterKeys;
    }


}