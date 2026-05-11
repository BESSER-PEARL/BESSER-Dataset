





import java.util.List;
import java.util.ArrayList;

public class statespace_Transition extends Storage {

    private int parameterCount;
    private int match;
    private String parameterKeys;



    public statespace_Transition(
        int parameterCount,        int match,        String parameterKeys    ) {
        super(
        );
        this.parameterCount = parameterCount;
        this.match = match;
        this.parameterKeys = parameterKeys;
    }


    public int getParametercount() {
        return parameterCount;
    }

    public void setParametercount(int parameterCount) {
        this.parameterCount = parameterCount;
    }
    public int getMatch() {
        return match;
    }

    public void setMatch(int match) {
        this.match = match;
    }
    public String getParameterkeys() {
        return parameterKeys;
    }

    public void setParameterkeys(String parameterKeys) {
        this.parameterKeys = parameterKeys;
    }


}